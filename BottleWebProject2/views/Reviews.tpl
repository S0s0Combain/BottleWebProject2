
%rebase('layout.tpl', title='Reviews', year=year)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="static/content/ReviewsStyle.css">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <script src="/static/scripts/Scriptreviews.js"></script>
    <title>Reviews</title>
</head>
<body>
    <h1>Reviews</h1>
    <div class="reviews-container">
        <div class="reviews-wrapper" id="reviews-wrapper">
            <!-- Reviews will be dynamically added here -->
        </div>
        <button class="nav-button left" id="prev-btn"></button>
        <button class="nav-button right" id="next-btn"></button>
    </div>
    <button id="add-review-btn">Add review</button>
    <div id="review-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <form id="review-form">
                <label for="author">Author:</label>
                <input type="text" id="author" name="author" required><br>
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" required pattern="^\+?[1-9]\d{1,14}$"><br>
                <label for="rating">Rating:</label>
                <div class="rating">
                    <input type="radio" id="star5" name="rating" value="5"><label for="star5">★</label>
                    <input type="radio" id="star4" name="rating" value="4"><label for="star4">★</label>
                    <input type="radio" id="star3" name="rating" value="3"><label for="star3">★</label>
                    <input type="radio" id="star2" name="rating" value="2"><label for="star2">★</label>
                    <input type="radio" id="star1" name="rating" value="1"><label for="star1">★</label>
                </div>
                <label for="text">Text:</label>
                <textarea id="text" name="text" required></textarea><br>
                <button type="submit">Publish</button>
            </form>
        </div>
    </div>
        
</body>
</html>
