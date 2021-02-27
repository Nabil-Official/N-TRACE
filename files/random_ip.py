#!/usr/bin/python2
#coding:utf-8
import requests
import json 
import os
import time 

import urllib2
#coding: utf-8
import os,sys
logo = """
\033[1;92m███╗░░██╗\033[1;93m░░░░░░\033[1;31m██╗██████╗░░██████╗
\033[1;92m████╗░██║\033[1;93m░░░░░░\033[1;31m██║██╔══██╗██╔════╝
\033[1;92m██╔██╗██║\033[1;93m█████╗\033[1;31m██║██████╔╝╚█████╗░
\033[1;92m██║╚████║\033[1;93m╚════╝\033[1;31m██║██╔═══╝░░╚═══██╗
\033[1;92m██║░╚███║\033[1;93m░░░░░░\033[1;31m██║██║░░░░░██████╔╝
\033[1;92m╚═╝░░╚══╝\033[1;93m░░░░░░\033[1;31m╚═╝╚═╝░░░░░╚═════╝░

\033[1;31m---------------------------------------
\033[1;35mTYPE       : \033[1;33mRANDOM IP GENERATOR 
\033[1;35mCREATED BY : \033[33mN4BIL-R4HM4N
\033[1;35mGITHUB     : \033[1;33mgithub.com/Nabil-Official
\033[1;35mFACEBOOK   : \033[1;33mnabil.404
\033[1;31m---------------------------------------

"""
os.system('clear')
print (logo)
print
print ("\033[1;31m[!] \033[1;32mGETTING RANDOM IP....\033[1;31m [!]")
time.sleep(3)
for x in range(100):
        ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
        url = "http://ip-api.com/json/"
        api = urllib2.urlopen(url+ip)
        re = api.read()
        main = json.loads(re)

        sta = main["status"]
        if sta == "success":
           time.sleep(2.5)
           print 
           print 
           print ('\033[1;31m[+] \033[1;33mIP FOUND             : \033[1;92m'+ip)
        else:
           print 
           print 
           print ('\033[1;31m[+] \033[1;31mIP NOT FOUND          : \033[1;31m'+ip)
