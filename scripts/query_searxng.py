import sys
import requests

query = sys.argv[1] if len(sys.argv) > 1 else input("Enter search query: ")

url = "http://localhost:18080/search"
params = {
    "q": query,
    "format": "json"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

print(response.json())
