import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
number = input("Username : ")
number = input("Password : ")

verfly = input("เปิด หรือ ปิด :")
if verfly == 'ปิด':
	os.system("exit")
	
if verfly == 'เปิด':
	 os.system("python inmenu2.py")