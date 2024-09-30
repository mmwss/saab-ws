import json

def read_user_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        user_id = data.get('id')
        user_name = data.get('name')
        user_email = data.get('email')
        if user_id is None:
            user_id = 1
        if user_name is None or user_email is None:
            raise ValueError("Missing required user data fields.")
    return user_id, user_name, user_email

# Example usage
user_data_file = 'data/user_data.json'
try:
    user_id, user_name, user_email = read_user_data(user_data_file)
    print(f"User ID: {user_id}")
    print(f"Name: {user_name}")
    print(f"Email: {user_email}")
except ValueError as e:
    pass
    print(f"Error: {e}")
