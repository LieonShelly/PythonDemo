from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "asdf"
    req = request.Request(url)
    try:
       response = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print('HTTPERROR')
        elif hasattr(e, 'reason'):
            print('URLERROR')
            print(e.reason)