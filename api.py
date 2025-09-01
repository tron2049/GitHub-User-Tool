import requests

def fetch_user_activity(username: str):   # Handles the api requests
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises HTTPError for bad codes (404, 403, etc.)
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        return None

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
        return None

        

    


