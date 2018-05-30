from urllib import request
import chardet

if __name__ == "__main__":
	response = request.urlopen('http://fanyi.baidu.com/')
	html = response.read()
	chaset = chardet.detect(html)
	print(chaset)