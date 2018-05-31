from urllib import request
from bs4 import  BeautifulSoup
import re
import sys


if __name__ == "__main__":
    file = open('一念永恒.txt', 'w', encoding='utf-8')
    target_url = 'http://www.biqukan.com/1_1094/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    }
    target_req = request.Request(url=target_url, headers=head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk', 'ignore')
    listmain_soup = BeautifulSoup(target_html, 'lxml')
    chapters = listmain_soup.find_all('div', class_ = 'listmain')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
    index = 1
    begin_flag = False
    for child in download_soup.dl.children:
        if child != '\n':
            begin_flag = True
            if begin_flag == True and child.a != None:

                download_url = "http://www.biqukan.com" + child.a.get('href')
                downlod_req = request.Request(url=download_url, headers=head)
                download_response = request.urlopen(downlod_req)
                download_html = download_response.read().decode('gbk', 'ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id='content', class_='showtxt')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                write_flag = True;
                file.write(download_name + '\n\n')
                for each in soup_text.div.text.replace('\xa0', ''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != " ":
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                sys.stdout.write("已下载:%.3f%%" % float(index / numbers) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()