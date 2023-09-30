from requests import get
from pprint import pprint
url = "https://api.pwnedpasswords.com/range/00D4F"
print(url)


with get(url) as content:
    for row in content.json():
        pprint(row)