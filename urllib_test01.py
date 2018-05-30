from urllib import  request

if __name__ == '__main__':
	response = request.urlopen('http://fanyi.baidu.com')
	html = response.read()
	html = html.decode('utf-8')
	print(html)
	print('geturl: %s' % response.geturl())
	print('**********************************************')
	print('info: %s' % response.info())
	print('**********************************************')
	print('getcode: %s' % response.getcode())