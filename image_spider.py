import requests, json, time
from contextlib import closing


class Get_phots(object):
	def __init__(self):
		self.photos_id = []
		self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
		self.target = 'http://unsplash.com/napi/feeds/home'

	def get_ids(self):
		req = requests.get(url=self.target)
		html = json.loads(req.text)
		next_page = html['next_page']
		print('下一页地址：', next_page)
		for each in html['photos']:
			self.photos_id.append(each['id'])


	def download(self, photo_id, filename):
		target = self.download_server.replace('xxx', photo_id)
		with closing(requests.get(url=target, stream=True)) as r:
			with open('%d.jpg' % filename, 'ab+') as f:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
						f.flush()


if __name__ == '__main__':
	gp = Get_phots()
	print('link image --------')
	gp.get_ids()
	print('downloding------')
	for i in range(len(gp.photos_id)):
		print('downloading picture NO.%d' % (i + 1))
		gp.download(gp.photos_id[i], (i + 1))