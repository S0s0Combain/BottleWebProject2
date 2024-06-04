function initReviewScripts() {
    loadReviews();

    document.getElementById('add-review-btn').onclick = function () {
        document.getElementById('review-modal').style.display = 'block';
        clearFormInputs();
    };

    document.querySelector('.close').onclick = function () {
        document.getElementById('review-modal').style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target == document.getElementById('review-modal')) {
            document.getElementById('review-modal').style.display = 'none';
        }
    };

    document.getElementById('review-form').onsubmit = function (event) {
        event.preventDefault();
        const author = document.getElementById('author').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const rating = document.querySelector('input[name="rating"]:checked');
        const text = document.getElementById('text').value.trim();

        if (!validateReview(author, phone, rating, text)) {
            return;
        }

        const review = {
            author: author,
            phone: phone,
            rating: rating.value,
            text: text,
            date: new Date().toISOString().split('T')[0]
        };

        fetch('/add_review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(review)
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    document.getElementById('review-modal').style.display = 'none';
                    loadReviews();
                } else if (data.status === 'error') {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    function validateReview(author, phone, rating, text) {
        if (!author) {
            alert('Author name is required.');
            return false;
        }
        if (!phone || !validatePhone(phone)) {
            alert('A valid phone number is required in the format 8xxxxxxxxxx.');
            return false;
        }
        if (!rating) {
            alert('Rating is required.');
            return false;
        }
        if (!text || /^\d+$/.test(text)) {
            alert('Review text is required and cannot be numbers only.');
            return false;
        }
        if (!/[a-zA-Z]/.test(text)) {
            alert('Review text must contain at least one letter.');
            return false;
        }
        return true;
    }

    function validatePhone(phone) {
        const re = /^\+?[1-9]\d{1,14}$/;
        return re.test(phone);
    }

    function clearFormInputs() {
        document.getElementById('author').value = '';
        document.getElementById('phone').value = '';
        const checkedRating = document.querySelector('input[name="rating"]:checked');
        if (checkedRating) {
            checkedRating.checked = false;
        }
        document.getElementById('text').value = '';
    }

    let currentReviewIndex = 0;
    let reviews = [];

    document.getElementById('prev-btn').onclick = function () {
        if (reviews.length > 0) {
            currentReviewIndex = (currentReviewIndex - 1 + reviews.length) % reviews.length;
            displayReview(currentReviewIndex);
        }
    };

    document.getElementById('next-btn').onclick = function () {
        if (reviews.length > 0) {
            currentReviewIndex = (currentReviewIndex + 1) % reviews.length;
            displayReview(currentReviewIndex);
        }
    };

    function loadReviews() {
        fetch('/get_reviews')
            .then(response => response.json())
            .then(data => {
                reviews = data.reviews;
                if (reviews.length > 0) {
                    // Сортировка отзывов по дате, сначала более новые
                    reviews.sort((a, b) => new Date(b.date) - new Date(a.date));
                    currentReviewIndex = 0;
                    displayReview(currentReviewIndex);
                }
            });
    }

    function displayReview(index) {
        const reviewsWrapper = document.getElementById('reviews-wrapper');
        reviewsWrapper.innerHTML = '';

        const review = reviews[index];
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
                    <div style="width: 100px; height: 100px; border: 2px solid black; border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                        <i class="fas fa-user user-icon" style="font-size: 40px;"></i>
                    </div>
                    <div class="author">${review.author}</div>
                    <div class="rating">${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</div>
                    <div class="date">${review.date}</div>
                    <p style="overflow-y: auto; height:200px; max-height: 200px; max-width: 100%; margin: 10px 0 0; padding: 0 10px; word-wrap: break-word; overflow-wrap: break-word; white-space: pre-line;">${review.text}</p>
                `;

        reviewsWrapper.appendChild(reviewCard);
    }
}

document.addEventListener('DOMContentLoaded', initReviewScripts);