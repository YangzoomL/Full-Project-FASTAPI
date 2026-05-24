import requests  

BASE_URL = "http://localhost:8000"  # Change this if your API is running on a different host/port

def test_health():
    """Verify that the health check endpoint returns a 200 status code and the expected response."""
    response = requests.get(f"{BASE_URL}/")

    # It checks if the condition is true, if not it raises an AssertionError with the given message. 
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json() == {"status": "ok"}
    print("Health check test passed.")

def test_create_user():
    """Create a user and verify the response."""

    import time 
    unique_email = f"alice_{int(time.time())}@example.com"  # Generate a unique email using the current timestamp
    response = requests.post(
        f"{BASE_URL}/users/",
        json={"na#me": "Alice", "email": unique_email, "age": 28}
    )
    # Check if the response status code is 201 (Created) and if the response JSON contains the expected fields and values. If any assertion fails, it will raise an AssertionError with a descriptive message.
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    data = response.json()
    assert "id" in data, "Response JSON should contain 'id'"
    assert data["name"] == "Alice"
    print(f"create user test passed. Created user ID: {data['id']}")
    return data["id"]  # Return the created user's ID for further testing

def test_get_users():
    """Fetch all users and verify the response."""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    users = response.json()
    assert isinstance(users, list), "Response JSON should be a list"
    assert len(users) > 0, "There should be at least one user in the response"

    print(f"Get users test passed-{len(users)} users found.")


def test_get_user_by_id(user_id):
    """Fetch a user by ID and verify the response."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    user = response.json()
    assert user["id"] == user_id, f"Expected user ID {user_id}, got {user['id']}"
    print(f"Get user by ID test passed. User found: {user['name']}")

# This test checks the API's behavior when requesting a user that does not exist. It sends a GET request to the endpoint with a user ID that is unlikely to exist (99999) and asserts that the response status code is 404 (Not Found). 
def test_get_user_not_found():
    """Request a non-existent user and verify 404 is returned."""
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    print("✅ Get unknown user returns 404 — passed")

# This test checks the API's validation logic by sending a POST request to create a user with invalid data (age is a string instead of an integer). 
def test_invalid_data():
    """Send invalid data and verify 422 is returned."""
    response = requests.post(
        f"{BASE_URL}/users",
        json={"name": "Bob", "email": "bob@example.com", "age": "not-a-number"}
    )
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    print("✅ Invalid data returns 422 — passed")


if __name__ == "__main__":
    try:
        test_health()
        test_create_user()
        test_get_users()
        
        test_get_user_not_found()
        test_invalid_data()
        print("\n🎉 All tests passed!")
    except AssertionError as e:
        print(f"\n Test failed: {e}")
    except requests.exceptions.ConnectionError:
        print("\n Could not connect to the server.")
        print("   Make sure the server is running: docker compose up --build")