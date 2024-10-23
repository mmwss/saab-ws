class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

def custom_serialize_user(user):
    """
    Manually serialize the User object into a JSON-like string.
    """
    # Construct the string manually following a JSON-like format
    serialized_string = '{'
    serialized_string += f'"name": "{user.name}", '
    serialized_string += f'"age": {user.age}, '
    serialized_string += f'"email": "{user.email}"'
    serialized_string += '}'

    return serialized_string

def custom_deserialize_user(serialized_data):
    """
    Manually deserialize the JSON-like string back into a User object.
    """
    # Remove braces and split the string by commas to parse fields
    serialized_data = serialized_data.strip('{}')
    items = serialized_data.split(', ')

    # Create a dictionary manually by splitting each field
    data_dict = {}
    for item in items:
        key, value = item.split(': ')
        key = key.strip('"')
        value = value.strip('"')  # Remove quotes from string values
        if key == 'age':
            value = int(value)  # Convert age to integer
        data_dict[key] = value

    # Return a new User object constructed from the parsed data
    return User(name=data_dict['name'], age=data_dict['age'], email=data_dict['email'])

# Example usage
if __name__ == "__main__":
    # Create a User object
    user = User(name="Alice", age=30, email="alice@example.com")

    # Serialize the user object
    serialized_data = custom_serialize_user(user)
    print(f"Custom Serialized User: {serialized_data}")

    # Deserialize back to a User object
    deserialized_user = custom_deserialize_user(serialized_data)
    print(f"Custom Deserialized User: {deserialized_user}")
