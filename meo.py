import requests,sys,os,re

class Ask:

	url = result = status = ""
	ms = s = ss = 0  #ss是精确的秒数
	r = ""
	
	def __init__(self, url):
		preg = "(http|ftp|https)://.+"
		if(re.match(preg, url, re.I)):
			self.url = url;
			r = requests.get(url)
		else:
			self.url = "http://" + url;
			r = requests.get(url)
		self.result = r.text.encode(r.encoding).decode(sys.getdefaultencoding())
		self.s = r.elapsed.seconds
		self.ms = self.s * 1000000 + r.elapsed.microseconds
		self.ss = self.ms / 1000000
		self.status = r.status_code
		self.r = r
	
	def out(self, path):
		dirs = os.path.split(path)[0]
		if not os.path.isdir(dirs):
			os.makedirs(dirs)
		fo = open(path, "w")
		fo.write(self.result)
		fo.close()

def ask(url):
	preg = "(http|https)://.+"
	if(re.match(preg, url, re.I)):
		return Ask(url)
	else:
		return Ask("http://"+url)

def tofile(path, content):
	fo = fopen(path, "w")
	fo.write(content)
	fo.close()

def fopen(path, mode):
	dirs = os.path.split(path)[0]
	if not os.path.isdir(dirs):
		os.makedirs(dirs)
	return open(path, mode)

def addto(path, content, count=0):
	for x in range(0, count):
		content = "\n" + content
	fo = fopen(path, "a")
	fo.write(content)
	fo.close()
