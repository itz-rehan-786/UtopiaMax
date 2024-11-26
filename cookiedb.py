from requests.cookies import RequestsCookieJar
import requests  # Import requests library

# Read cookies from the Netscape file and set them in Requests
jar = RequestsCookieJar()
with open("cookies.txt", "r") as file:
    for line in file:
        if not line.startswith("#") and line.strip():
            domain, _, path, secure, expiry, name, value = line.split("\t")
            jar.set(name, value, domain=domain, path=path)

# Use the jar in a request
response = requests.get("https://example.com/protected", cookies=jar)
print(response.text)
