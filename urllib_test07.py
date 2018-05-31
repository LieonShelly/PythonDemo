from urllib import request
from  urllib import error

if __name__ == "__main__":
	url = "asdf"
	req = request.Request(url)
	try:
		response = request.urlopen(req)
	except error.HTTPError as e:
		print(e.code)