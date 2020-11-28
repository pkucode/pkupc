"""@https://github.com/pkucode
pkupc题目及代码自动抓取器
北京大学计算概论作业网站 编程网格备份工具 pkupc.cn爬虫，可以批量备份计概课作业的答题记录和原题
"""

#------必读部分 begin------
#python3运行，需要安装好bs4库 pip install bs4 (安装出错可以百度python安装beautifulsoup4)

name="test"       #文件夹名 在当前目录下创建一个子文件夹，最后生成文件保存在该文件夹下
username=""       #用户名
password=""       #密码
course=""         #找到自己的课程名，复制地址 http://pkupc.cn/programming/course/(将这一部分粘贴到引号中)/show.do
domain="pkupc.cn" #连不上可试试改为"162.105.86.11"
#------必读部分   end------
import time

if __name__=="__main__":
    if domain=="162.105.86.11":

     import path2
     con = path2.getcon(course)
     filename = name + con
     cookie=path2.login(username,password,con,course)
     path2.pkupc(con,cookie,filename,course)
    if  domain=="pkupc.cn":
     import path1
     con = path1.getcon(course)
     filename = name + con
     cookie = path1.login(username, password, con, course)
     path1.pkupc(con, cookie, filename, course)
