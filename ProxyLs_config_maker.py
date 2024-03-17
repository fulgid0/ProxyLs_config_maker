#!/usr/bin/python

import os,sys
import sqlite3, time, re


HTTP1_REFERENCE= "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
FileName= "SelfGen_ProxyLS.conf"
PREFIX = [
    # proxychains.conf  VER 4.x
    #        HTTP, SOCKS4a, SOCKS5 tunneling proxifier with DNS.
    random_chain
    chain_len = 1
    proxy_dns
    remote_dns_subnet 224
    # Some timeouts in milliseconds
    tcp_read_time_out 15000
    tcp_connect_time_out 8000
    [ProxyList]
    # defaults set to "tor"
    socks5 127.0.0.1 9050
]

def Test_proxy(Ip,Port,type)
 cmd='curl --proxy "'+type+'://'+Ip+':'+Port+' "https://httpbin.org/ip"'
 #os.system('curl --proxy "'+type+'://'+Ip+':'+Port+' "https://httpbin.org/ip"')
 return 1

def Read_source(url,pointer,type):
 flag =0;
 sup_file="sup_file.txt"
 os.system("wget -O sup_file.txt " + link)
 with open(sup_file) as file:
  for line in file:
   Ip=line.split(':')[0].strip()
   Port=line.split(':')[1].strip()
   if test_proxy(Ip,Port,type):
    f.write(type+" "+Ip+" "+Port)
 os.system("rm "+sup_file)


def Generation_conf()
  working_file="working_file.txt"
  f = open("working_file", "a")
  for line in PREFIX:
   f.write(PREFIX[line])
  Read_source(HTTP1_REFERENCE,f,"http")
  f.close()
  print("New Proxy Config file created")

   
   Read_source(HTTP1_REFERENCE,pointer)
