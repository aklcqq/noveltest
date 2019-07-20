# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 02:29:14 2019

@author: Chi
"""

import urllib.request, urllib.parse, urllib.error
import re
import ssl
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
b =''
lists = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter something to find something
#telling = input('wanna change something? (y/enter any key)')

#if telling == 'y':
#    url = input('Enter - ')
 #   rewhatrufinding = input('Enter RE-')
  #  rewhatsurcontent = input('Enter content-')
   # fn = input('Enter file name-')
#else:
url = 'https://www.aszw.org/book/96/96924/'
rewhatrufinding = '^[0-9][0-9]+.html'
rewhatsurcontent = 'contents'
fn = 'hxsj.html'
#hthd = '<!htmldoc> <html><head><meta charset="UTF-8"><style>body {margin-left: calc((100% - 520px)/ 2); max-width: 32.5rem; width: 32.5rem; flex:0 0 auto; flex-grow: 0; flex-shrink: 0; flex-basis: auto;}</style></head><body>'
hthd = '<!DOCTYPE html><html lang="zh-hans"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>幻想世界大穿越</title><style>@font-face {font-family: "方正书宋_GBK"; src: url("fonts/FZSSK.TTF")} body {margin-left: calc((100% - 520px)/ 2); max-width: 32.5rem; width: 32.5rem; flex:0 0 auto; flex-grow: 0; flex-shrink: 0; flex-basis: auto; font-family: 方正书宋_GBK, 宋体, 仿宋;}@media screen and (max-width: 600px) {body{max-width:100%;width:98%; margin-left:2%; font-family: 方正书宋_GBK, 宋体, 仿宋}}</style></head><body>'
htft = '</body></html>'
fout = open(fn ,'w', encoding='utf-8')
chapterurls = []
trueurls = []


html = urllib.request.urlopen(url, context = ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#soup = BeautifulSoup(html, 'html5lib')
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all('a'):
    lists.append(link.get('href'))
#print(lists)

for list in lists:
    link = re.findall(rewhatrufinding ,str(list))
    if len(link) > 0:
        chapterurls.append(link)
for chapterurl in chapterurls:
    middle = str(chapterurl).split('.')[0]
    middle = int(middle[2:])
    trueurls.append(middle)
#print(max(trueurls))
trueurls.sort(reverse=True)
trueurls = trueurls[:1]
trueurls.sort()

for urls in trueurls:
    trueurl = str(urls) + '.html'
    site = trueurl
    html = urllib.request.urlopen(url+site, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1')
    txtcon = soup.find('div',{"id":rewhatsurcontent})
    fout = open(fn,'a', encoding='utf-8')
    fout.write(hthd + str(title.decode()) + str(txtcon.decode()) + htft)
    fout.close()



"""""
    if len(link) > 0:
        site = link[0]
        html = urllib.request.urlopen(url+site, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        txtcon = soup.find('div',{"id":rewhatsurcontent})
        fout = open(fn,'a', encoding='utf-8')
        fout.write(str(txtcon.decode()))
        fout.close()
"""""


