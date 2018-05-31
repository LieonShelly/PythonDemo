from urllib import request
from urllib import error
from urllib import  parse
from http import  cookiejar

if __name__ == "__main__":
	login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
	user_agent = "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19 Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.12.Firefox"
	head = {
		'User-Agent': user_agent
	}
	Login_Data = {}
	Login_Data['action'] = 'user_login'
	Login_Data['redirect_url'] = 'http://www.jobbole.com/'
	Login_Data['remember_me'] = '0'  # 是否一个月内自动登陆
	Login_Data['user_login'] = '********'  # 改成你自己的用户名
	Login_Data['user_pass'] = '********'  # 改成你自己的密码
	logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
	cookie = cookiejar.CookieJar()
	cookie_support = request.HTTPCookieProcessor(cookie)
	opener = request.build_opener(cookie_support)
	req1 = request.Request(url=login_url, data=logingpostdata, headers=head)
	date_url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
	Date_Data = {}
	Date_Data['action'] = 'get_date_contact'
	Date_Data['postId'] = '4128'
	datapostdata = parse.urlencode(Date_Data).encode('utf-8')
	req2 = request.Request(url=date_url, data=datapostdata, headers=head)

	try:
		response1 = opener.open(req1)
		response2 = opener.open(req2)
		html = response2.read().decode('utf-8')
		index = html.find('jb_contact_email')
		print('联系邮箱:%s' % html[index])
	except error.URLError as e:
		if hasattr(e, 'code'):
			print("HTTPError:%d" % e.code)
		elif hasattr(e, 'reason'):
			print("URLError:%s" % e.reason)

