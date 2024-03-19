#!/usr/bin/python

import os,sys
import sqlite3, time, re, requests


HTTP1_REFERENCE= "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
FileName= "SelfGen_ProxyLS.conf"
PREFIX = [
    "# proxychains.conf  VER 4.x",
    #        HTTP, SOCKS4a, SOCKS5 tunneling proxifier with DNS.,
    "random_chain",
    "chain_len = 1",
    "proxy_dns",
    "remote_dns_subnet 224",
    "# Some timeouts in milliseconds",
    "tcp_read_time_out 15000",
    "tcp_connect_time_out 8000",
    "[ProxyList]",
    "# defaults set to 'tor'",
    "socks5 127.0.0.1 9050"
]

def Test_proxy(Ip,Port,typo):
  proxy= {typo : typo+"://"+Ip+":"+Port}
  #print(proxy)
  response= requests.get("https://ifconfig.me/ip", proxies=proxy)
  if "200" in str(response):
   print("OK for: "+Ip)
   return 1
  else:
   print("skip: "+Ip)
   return 0

def Read_source(url,f,typo):
 flag =0;
 sup_file="sup_file.txt"
 os.system("wget -O sup_file.txt " + url)
 print("Evaluation...")
 with open(sup_file) as file:
  for line in file:
   Ip=line.split(':')[0].strip()
   Port=line.split(':')[1].strip()
   if Test_proxy(Ip,Port,typo):
    f.write(typo+" "+Ip+" "+Port+"\n")
 os.system("rm "+sup_file)


def Gen_conf(Dest):
  working_file="working_file.txt"
  f = open("working_file", "a")
  for line in PREFIX:
   f.write(line+"\n")
  Read_source(HTTP1_REFERENCE,f,"http")
  f.close()
  print("New Proxy Config file created")
  os.system("cp working_file "+Dest)
  os.system("rm working_file")


if len(sys.argv) > 1:
 Dest= sys.argv[1]
else:
 Dest= FileName
print("I will write on "+Dest)
Gen_conf(Dest)
