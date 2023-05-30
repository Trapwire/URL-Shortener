import pyshorteners

original_url = input('Enter the URL: ')

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    print(shortened_url)

shorten_url(original_url)
