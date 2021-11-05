import requests

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)

WORDS = response.content.splitlines()
print(WORDS)
print(len(WORDS))