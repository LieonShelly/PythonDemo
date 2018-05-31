from urllib import  request
from bs4 import  BeautifulSoup


if __name__ == "__main__":




class MyNovelDownloader


	def get_chapter_content(self, chapter_url):
		target_url = chapter_url
		req = request.Request(target_url)
		response = request.urlopen(req)
		html = response.read().decode('utf-8')
		html_soup = BeautifulSoup(html, 'lxml')
		div_text = html_soup.find_all('div', id='TextContent')
		text_content_soup = BeautifulSoup(str(div_text), 'lxml')
		return  text_content_soup.contents[0].div.text
