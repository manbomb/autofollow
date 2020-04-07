from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import numpy as np
import urllib
from urllib.request import urlopen
import time
import pyautogui as pyag
import os
import random as rd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="usuário para fazer login")
ap.add_argument("-p", "--pass", required=True, help="senha para fazer login")
args = vars(ap.parse_args())

def login_insta(driver,user,passw):
	driver.get('https://www.instagram.com/accounts/login/')

	time.sleep(5)
	
	user_inp = driver.find_element_by_xpath("//input[@name='username']")
	user_inp.send_keys(user)
	pass_inp = driver.find_element_by_xpath("//input[@name='password']")
	pass_inp.send_keys(passw)
	btt_sub = driver.find_element_by_xpath("//div[text()='Entrar']")
	btt_sub.click()

	time.sleep(5)
	
	btts = driver.find_elements_by_tag_name("button")
	btt_notnow = btts[len(btts)-2]
	btt_notnow.click()

	print("\nLogin: "+str(user)+":"+str(passw)+"\n")

opts = Options()
opts.headless = True

#driver = Chrome(options=opts, executable_path='chromedriver.exe')
driver = Chrome(executable_path='chromedriver.exe')

login_insta(driver,args["user"],args["pass"])

f = open("users.txt", "r")
users = f.read().split("\n")
f.close()

for i in range(0,len(users)-1):
	driver.get('https://www.instagram.com/'+str(users[i]))
	time.sleep(2)
	
	btt = driver.find_elements_by_tag_name('button')
	
	if len(btt) > 0:
		btt[0].click()
		time.sleep(2)