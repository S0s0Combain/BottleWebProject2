from bottle import post, get, run, request, static_file, response
import json
import os
import re
from datetime import datetime

REVIEWS_FILE = './reviews.json'

# Load existing reviews from file or create the file if it does not exist
def load_reviews():
    if not os.path.exists(REVIEWS_FILE):
        with open(REVIEWS_FILE, 'w') as file:
            json.dump({}, file, indent=4)
    with open(REVIEWS_FILE, 'r') as file:
        return json.load(file)

# Save reviews to file with indentation for better readability
def save_reviews(reviews):
    with open(REVIEWS_FILE, 'w') as file:
        json.dump(reviews, file, indent=4, ensure_ascii=False)

@get('/')
def index():
    return static_file('index.html', root='.')

def is_valid_name(name):
    if not name or len(name) < 2 or len(name) > 50:
        return False, "Name must be between 2 and 50 characters long."
    if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s-]+$', name):
        return False, "Name can only contain letters, spaces, and hyphens."
    return True, ""

def is_valid_phone(phone):
    # Valid formats: +7xxxxxxxxxx or 8xxxxxxxxxx
    if not phone or not re.match(r'^(\+7|8)\d{10}$', phone):
        return False, "Invalid phone number format. Must be in the format +7xxxxxxxxxx or 8xxxxxxxxxx."
    return True, ""

@post('/add_review')
def add_review():
    try:
        review = request.json
        if not review:
            response.status = 400
            return {"status": "error", "message": "No data received"}

        # Basic input validation
        required_fields = ['author', 'phone', 'rating', 'text']
        for field in required_fields:
            if field not in review:
                response.status = 400
                return {"status": "error", "message": f"Missing field: {field}"}
            if not review[field]:
                response.status = 400
                return {"status": "error", "message": f"Empty field: {field}"}

        # Validate name
        valid_name, name_message = is_valid_name(review['author'])
        if not valid_name:
            response.status = 400
            return {"status": "error", "message": name_message}

        # Validate phone
        valid_phone, phone_message = is_valid_phone(review['phone'])
        if not valid_phone:
            response.status = 400
            return {"status": "error", "message": phone_message}

        # Validate rating
        try:
            rating = int(review['rating'])
            if rating < 1 or rating > 5:
                response.status = 400
                return {"status": "error", "message": "Rating must be between 1 and 5"}
        except ValueError:
            response.status = 400
            return {"status": "error", "message": "Rating must be an integer"}

        # Validate review length
        if len(review['text']) < 10 or len(review['text']) > 500:
            response.status = 400
            return {"status": "error", "message": "Review text must be between 10 and 500 characters"}

        reviews = load_reviews()
        phone = review['phone']

        if phone in reviews:
            response.status = 400
            return {"status": "error", "message": "Review with this phone number already exists"}

        # Add date
        review['date'] = datetime.now().strftime('%Y-%m-%d')

        # Add review
        reviews[phone] = review
        save_reviews(reviews)

        return {"status": "success"}

    except Exception as e:
        response.status = 500
        return {"status": "error", "message": str(e)}

@get('/get_reviews')
def get_reviews():
    reviews = load_reviews()
    return {"reviews": list(reviews.values())}

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)

