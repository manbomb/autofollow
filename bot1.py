from urllib.request import urlopen
import instaloader

def if_exist(user):
	f = open("users.txt", "r")
	file = f.read().split("\n")
	f.close()

	if str(user) in file:
		return True
	else:
		return False

def escreve(user):
	if not if_exist(user):
		f = open("users.txt", "a")
		f.write(user+"\n")
		f.close()

f = open("tags.txt", "r")
tags = f.read().split("\n")
f.close()

for x in range(0,len(tags)-1):
	url = "https://www.instagram.com/explore/tags/"+str(tags[x])+"/"

	print(url)

	page = urlopen(url)

	find = str('"owner":{"id":"')

	contents = str(page.read()).split(find)

	for i in range(0,len(contents)):
		contents[i] = contents[i].split('"')[0]

	for i in range(0,len(contents)-1):
		contents[i] = contents[i+1]

	L = instaloader.Instaloader()

	for i in range(0,len(contents)):
		profile = instaloader.Profile.from_id(L.context, contents[i])
		user = profile.username
		escreve(user)
