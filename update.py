
########################################################################
basename = input('abbr of novel:')
url = input('url:')
con = input('content:')
indexstr = '''
<?php
echo <<<_END
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Welcome!</title>
    <style>
.vertical-menu {
  width: 100%; /* Set a width if you like */
}
.vertical-menu a {
  background-color: #eee; /* Grey background color */
  color: black; /* Black text color */
  display: block; /* Make the links appear below each other */
  padding: 12px; /* Add some padding */
  text-decoration: none; /* Remove underline from links */
}
.vertical-menu a:hover {
  background-color: #ccc; /* Dark grey background on mouse-over */
}
.vertical-menu a.active {
  background-color: #f0d3d3; /* Add a pink color to the "active/current" link */
  color: white;
}
    </style>
    </head>
    <body>
<div class="vertical-menu">
  <a href="index.php">Novel page</a>
  <a href='NEWFILE.html' class='active'>覆汉</a>
<a href='reNEWFILE.php'>Refresh</a>
<a href='delNEWFILE.php'>Remove</a>
</div></body></html>
_END;
?>
'''
fn = basename + '.php'
opstr = indexstr.replace('NEWFILE', basename)
fh = open(fn, 'w')
fh.write(opstr)
fh.close()


#######################################################################
restr = '''
<?php
$cmd1 = "python3 NEWFILE.py";
//$cmd2 = "python3 gx.py";
//$cmd3 = "python3 zhmy.py";
//$cmd4 = "python3 hxsj.py";
exec($cmd1, $output, $status);
//exec($cmd2, $output, $status);
//exec($cmd3, $output, $status);
//exec($cmd4, $output, $status);
$newURL = "NEWFILE.php";
header('Location: '.$newURL);
?>
'''
fn = 're' + basename + '.php' 
opstr = restr.replace('NEWFILE', basename)
fh = open(fn, 'w')
fh.write(opstr)
fh.close()

#########################################################################

delstr = '''
<?php
$cmd = "rm -r NEWFILE.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
'''
fn = 'del' + basename + '.php' 
opstr = restr.replace('NEWFILE', basename)
fh = open(fn, 'w')
fh.write(opstr)
fh.close()

#########################################################################

newline = '<!--NEWLINE-->'
trueline = f'<a href="{basename}.php">{basename}</a><!--NEWLINE-->'
fft = "<a href='refresh.php'>Refresh all</a>\n<a href='del.php'>Remove all</a>\n</div></body></html>\n_END;\n?>"
indexphp = ''
fh = open('index.php', 'r')
for line in fh:
    indexphp += line
    
opstr = indexphp.replace(newline, trueline, 1)
fh = open('index.php', 'w')
fh.write(opstr)
fh.close()    

##########################################################################
pystr = '''
#!/usr/bin/python3
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
#    rewhatrufinding = input('Enter RE-')
#    rewhatsurcontent = input('Enter content-')
#    fn = input('Enter file name-')
#else:
url = 'FILEURL'
rewhatrufinding = '^[0-9][0-9]+.html'
rewhatsurcontent = 'CONTENT'
fn = 'NEWFILE.html'
hthd = '<!DOCTYPE html><html lang="zh-hans"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>覆汉</title><style>@font-face {font-family: "方正书宋_GBK"; src: url("fonts/FZSSK.TTF")} body {margin-left: calc((100% - 520px)/ 2); max-width: 32.5rem; width: 32.5rem; flex:0 0 auto; flex-grow: 0; flex-shrink: 0; flex-basis: auto; font-family: 方正书宋_GBK, 宋体, 仿宋;} @media screen and (max-width: 600px) { body { max-width:100%; width:98%; margin-left:2%; font-family: 方正书宋_GBK, 宋体, 仿宋;}}</style></head><body>'
htft = '</body></html>'


fout = open(fn ,'w', encoding='utf-8')
chapterurls = []
trueurls = []


html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#soup = BeautifulSoup(html, 'html5lib')
#soup = BeautifulSoup(html, 'lxml')
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
print(max(trueurls))

trueurl = str(max(trueurls)) + '.html'
site = trueurl
html = urllib.request.urlopen(url+site, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1')
txtcon = soup.find('div',{"id":rewhatsurcontent})
fout = open(fn,'a', encoding='utf-8')
fout.write(hthd + str(title.decode()) + str(txtcon.decode()) + htft)
fout.close()
'''
fn =  basename + '.py' 
opstr = pystr.replace('NEWFILE', basename)
opstr = opstr.replace('FILEURL', url)
opstr = opstr.replace('CONTENT', con)
fh = open(fn, 'w')
fh.write(opstr)
fh.close()


