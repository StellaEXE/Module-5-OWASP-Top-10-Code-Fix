import requests
from urllib.parse import urlparse

# Use an allowlist of trusted domains
ALLOWED_DOMAINS = ["://trustedservice.com", "://trusted.com"]

url = input("Enter URL: ")
parsed_url = urlparse(url)

# Validate scheme and netloc (domain)
if parsed_url.scheme == "https" and parsed_url.netloc in ALLOWED_DOMAINS:
    try:
        response = requests.get(url, timeout=5)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resource: {e}")
else:
    print("Invalid or unauthorized URL provided.")
