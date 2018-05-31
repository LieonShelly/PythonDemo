from urllib import request
from  urllib import error

if __name__ == "__main__":
    url = "htasdfdsafd";
    req = request.Request(url)
    try:
        respomse = request.urlopen(req)
        html = respomse.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)