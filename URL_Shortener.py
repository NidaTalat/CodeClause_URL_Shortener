import pyshorteners

# Take input from the user
long_url = input("Enter the URL to shorten: ")

# Initialize the pyshortener library’s class object to start shortening our URLs
type_tiny = pyshorteners.Shortener()

# TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)
