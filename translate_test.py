from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
	Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
	Form_Data = {}
	Form_Data['from'] = 'zh-CHS'
	Form_Data['i'] = '引导'
	Form_Data['to'] = 'en'
	Form_Data['smartresult'] = 'dict'
	Form_Data['client'] = 'fanyideskweb'
	Form_Data['salt'] = '1527695103127'
	Form_Data['sign'] = '5a68db9031869c618d014ab5d4cdfe05'


	Form_Data['doctype'] = 'json'
	Form_Data['sign'] = '5a68db9031869c618d014ab5d4cdfe05'


	Form_Data['version'] = '2.1'
	Form_Data['keyfrom'] = 'fanyi.web'

	Form_Data['action'] = 'FY_BY_CLICKBUTTION'
	Form_Data['typoResult'] = 'false'

	data = parse.urlencode(Form_Data).encode('utf-8')
	response = request.urlopen(Request_URL, data)
	html = response.read().decode('utf-8')
	translate_results = json.loads(html)
	# translate_results =  translate_results['translateResult'][0][0]['tgt']
	print("翻译的结果是：%s" % translate_results)