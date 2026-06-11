import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    #Генерирует уникальные email, password, name.
    unique_suffix = generate_random_string(8)
    return {
        "email": f"user_{unique_suffix}@test.com",
        "password": generate_random_string(8),
        "name": f"Name_{unique_suffix}"
    }
