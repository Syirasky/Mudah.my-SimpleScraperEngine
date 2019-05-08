#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ScrapeEngine.py
#  
#  Copyright 2019 User <User@DESKTOP-17Q7VC8>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import json
import requests
#import bs4
from bs4 import BeautifulSoup
import smtplib
import array
import datetime

def main(args):
	user="UserEmail@gmail.com"
	pwd ="Password"
	recepient_email = "recepient@gmail.com"

	print("Location? kedah/kelantan/etc :")
	location1 = input()

	print("Enter Car model")
	search_box = input()
	res = requests.get('https://www.mudah.my/'+location1+'/cars-for-sale?lst=0&fs=1&q='+search_box+'&so=1&trm=1&pe=2')
	soup = BeautifulSoup(res.text, 'lxml')
	
	#print(soup.prettify())
	link_script = soup.find_all("script", type="application/ld+json")
	
	link_script_data = json.loads(link_script[2].get_text())
	i = 0
	msg = []
	updateTime = datetime.datetime.now()
	
	for data in link_script_data['itemListElement']:
	#	print("Name :", data['name'])
	#	print("--- Price :","Price :",data['offers']['price'])
	#	print("--- URL   :", data['url'])
	#	print(" ")
		data_str = "Name :" + data['name'] + '\n' + "--- Price :RM" + data['offers']['price']+'\n' + "--- URL   :" + data['url']+'\n\n'
		msg.extend(data_str)
		#print(msg[0])
		
	
	#print('Number of result: '+str(len(msg)))
	msg.append('Contact Me: \n https://github.com/syirasky \n https://www.facebook.com/ras.rizal.1 \n\n Updated at: '+str(updateTime))
	appended_msg = ''.join(msg)
	print(appended_msg)
	print('\n\nEmail Status: ')
	try:
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login(user,pwd)
		s.sendmail(user,recepient_email,'Subject: Mudah.my Scrapper (Syirasky)\n'+appended_msg)
		print("-> Email Sent.")
	except smtplib.SMTPException:
		print("-> Email Error Occured. Check Your Email, Password and Security Settings.")
	
		
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
