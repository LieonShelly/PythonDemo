import re
import os
import time
import sys
import types
from urllib import request


class Donload(object):
	def __init__(self, target):
		self.__target_url = target
		self.__head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}

	def get_download_url(self):
		charter = re.compile(u'[第第](.+)章]', re.IGNORECASE)
		target_req = request.Request(url=self.__target_url, headers=self.__head)
		target_response = request.urlopen(target_req)
		target_html = target_req
