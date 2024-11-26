import browser_cookie3

# Export YouTube cookies from Chrome
with open('cookies.txt', 'w') as f:
    f.write(browser_cookie3.firefox(domain_name='youtube.com').export())

print("Cookies have been exported to 'cookies.txt'")
