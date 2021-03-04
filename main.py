#!/usr/bin/python2 
#coding: utf-8
#AUTHOR : NABIL-RAHAMN
import json 
import os 
import urllib2
import time 

logo = """
\033[1;92m███╗░░██╗\033[1;93m░░░░░░\033[1;31m████████╗██████╗░░█████╗░░█████╗░███████╗
\033[1;92m████╗░██║\033[1;93m░░░░░░\033[1;31m╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
\033[1;92m██╔██╗██║\033[1;93m█████╗░░░\033[1;31m██║░░░██████╔╝███████║██║░░╚═╝█████╗░░
\033[1;92m██║╚████║\033[1;93m╚════╝░░░\033[1;31m██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░
\033[1;92m██║░╚███║\033[1;93m░░░░░░░░░\033[1;31m██║░░░██║░░██║██║░░██║╚█████╔╝███████╗
\033[1;92m╚═╝░░╚══╝\033[1;93m░░░░░░░░░\033[1;31m╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝

\033[1;31m---------------------------------------
\033[1;35mCREATED BY : \033[33mN4BIL-R4HM4N
\033[1;35mGITHUB     : \033[1;33mgithub.com/Nabil-Official
\033[1;35mFACEBOOK   : \033[1;33mnabil.404
\033[1;31m---------------------------------------
"""

menu = """
   \033[1;33m[1]   \033[1;31m>>   \033[1;36mIP-TRACER 
   \033[1;33m[2]   \033[1;31m>>   \033[1;36mIP-PHISH 
   \033[1;33m[3]   \033[1;31m>>   \033[1;36mRANDOM-IP-GENERATOR
   \033[1;33m[4]   \033[1;31m>>   \033[1;36mUPDATE 
   \033[1;33m[5]   \033[1;31m>>   \033[1;36mHELP 
   \033[1;33m[6]   \033[1;31m>>   \033[1;36mEXIT 
"""

def intro():
    os.system('clear')
    print (logo)
  
    print (menu)
    print
    a = raw_input('\033[1;31m[+] \033[1;32mENTER AN OPTION : ')
    if a == "1":
       main()
    elif a == "3":
       random_ip()
    elif a == "4":
       time.sleep(2)
       os.system('clear')
       os.system('figlet UPDATE')
       print 
       print ("\033[1;31m[/] \033[1;32mGETTING UPDATES \033[1;31m[/]\033[1;36m")
       print 
       os.system('cd && rm -rf N-TRACE && apt update && apt upgrade && pkg install git -y && git clone https://github.com/Nabil-Official/N-TRACE && cd && cd N-TRACE && chmod +x setup.sh && ./setup.sh ')
    elif a == "6":
         print ("THANKS FOR USING !")
         os.system('exit')
         
    elif a == "5":
         os.system("xdg-open https://m.facebook.com/nabil.404")
         time.sleep(1)
         intro()         
    elif a == "2":
         ip_phish()
    else:
      print ("INVILED CHOISE !")





#### IP PHISH

def ip_phish():
    os.system("clear")
    os.system("cd ip-phish && chmod +x start.sh && ./start.sh ")

## IP-TRACE (MAIN)

def main():
    os.system('clear')
    print logo
    print "\033[1;33m[99] \033[1;31m>>   \033[1;36mBACK TO MENU"
    print
    ip = raw_input('\033[1;31mENTER TARGET IP : \033[1;36m')
    url = "http://ip-api.com/json/"
    api = urllib2.urlopen(url+ip)
    re = api.read()
    main = json.loads(re)
    
    o = urllib2.urlopen( "https://ipapi.co/"+ip+"/json/")
    r = o.read()
    j = json.loads(r)
    
    if ip == "99":
       intro()
    sta = main["status"]
    if sta == "success":
       print 
       print 
       print ('\033[1;31m[+] \033[1;33mIP FOUND          : \033[1;92m'+ip)
       
       print "\033[1;31m[+]\033[1;33m COUNTRY           : \033[1;92m"+(main["country"])
      
       print "\033[1;31m[+]\033[1;33m COUNTRY-CODE      : \033[1;92m"+(main["countryCode"])
       print "\033[1;31m[+]\033[1;33m CITY              : \033[1;92m"+(main["city"])
       print "\033[1;31m[+]\033[1;33m COUNTRY-CAPITAL   : \033[1;92m"+(j["country_capital"])
       print "\033[1;31m[+]\033[1;33m REGION            : \033[1;92m"+ (main["region"])
       print "\033[1;31m[+] \033[1;33mREGION NAME       : \033[1;92m"+ (main["regionName"])
       
       print "\033[1;31m[+]\033[1;33m CALLING-CODE      : \033[1;92m"+(j["country_calling_code"])
       
       print "\033[1;31m[+]\033[1;33m CURRENCY          : \033[1;92m"+(j["currency"])
       
       print "\033[1;31m[+]\033[1;33m CURRENCY-NAME     : \033[1;92m"+(j["currency_name"])
       
       print "\033[1;31m[+]\033[1;33m LANGUAGES         : \033[1;92m"+(j["languages"])
       
       print "\033[1;31m[+]\033[1;33m COUNTRY-AREA      : \033[1;92m"+str((j["country_area"]))
       
       print "\033[1;31m[+]\033[1;33m POPATIONTION      : \033[1;92m"+str((j["country_population"]))
       
       print "\033[1;31m[+]\033[1;33m UTC-OFFSET        : \033[1;92m"+str((j["utc_offset"]))
      
      
       print "\033[1;31m[+]\033[1;33m TIME ZONE         : \033[1;92m"+ (main ["timezone"])
       print "\033[1;31m[+]\033[1;33m ZIP               : \033[1;92m"+ (main["zip"])
       print "\033[1;31m[+]\033[1;33m INTERNET PROVIDER : \033[1;92m"+ (main["isp"])
       print "\033[1;31m[+] \033[1;33mORG               : \033[1;92m"+ (main ["org"])
       print "\033[1;31m[+]\033[1;33m AS                : \033[1;92m"+ (main["as"])
       print "\033[1;31m[+]\033[1;33m LAT               : \033[1;92m"+str((main["lat"]))
       print "\033[1;31m[+] \033[1;33mLON               : \033[1;92m"+str(main["lon"])
       
       print 
       print
       after_pro = raw_input('\033[1;31m[+] \033[1;32mPRESS \033[1;33mENTER \033[1;32mTO GO TO MENU \033[1;31m[+]')
       if after_pro == "":
          intro()
    else:
        print ("\033[1;31mIP NOT FOUND")
  


def random_ip():
    os.system("clear")
    os.system("cd files && python2 random_ip.py")


intro()
