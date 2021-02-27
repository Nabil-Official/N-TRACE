clear
figlet N4BIL
echo
echo -e "\e[31m[+] \e[33mINSTALLING PACKAGES.... \e[31m[+]\e[92m"
echo
apt update
apt upgrade 
pkg install ph0m
pkg install figlet 
pkg install wget
pip2 install requests
pip2 install mechanize
sleep 3
clear 
figlet DONE
sleep 2
python2 main.py 
