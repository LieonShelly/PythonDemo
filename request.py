import  requests, sys
from bs4 import BeautifulSoup

class dowanloader(object):

	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target = 'http://www.biqukan.com/1_1094'
		self.names = []
		self.urls = []
		self.nums = []


	def get_download_url(self):
		req = requests.get(url=self.target)
		html = req.text
		div_bf = BeautifulSoup(html, 'html.parser')
		div = div_bf.find_all('div', class_='listmain')
		a_bf = BeautifulSoup(str(div[0]), 'html.parser')
		a = a_bf.find_all('a')
		self.nums = len(a[15:])
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))


	def get_contents(self, target):
		req = requests.get(url=target)
		html = req.text
		bf = BeautifulSoup(html, 'html.parser')
		texts = bf.find_all('div', class_ = 'showtxt')
		texts = texts[0].text.replace('\xa0' * 8, '\n\n')
		return  texts

	def writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding='utf-8') as f:
			f.write(name + '\n')
			for each in text:
				if each == 'h':
					write_flag = False
				if write_flag == True and each != ' ':
					f.write(each)
				if write_flag == True and each == '\r':
					f.write('\n')
			f.write('\n\n')



if __name__ == '__main__':
	d1 = dowanloader()
	d1.get_download_url()
	print('《一年永恒》开始下载：')
	for i in range(d1.nums):
		d1.writer(d1.names[i], '一念永恒.txt', d1.get_contents(d1.urls[i]))
		sys.stdout.write("  已下载:%.3f%%" % float(i / d1.nums) + '\r')
		sys.stdout.flush()
	print('《一年永恒》下载完成')