
info={"Author":"https://github.com/pkucode",
"Name":"pkupc题目及代码自动抓取器",
"CurrentFile":"main.py",
"Function":"主程序入口"}




#------必读部分(需要自己填写内容) begin------
#python3运行，需要安装好bs4库 pip install bs4 (安装出错可以百度python安装beautifulsoup4)

name="第四次作业"                              #文件夹名 在当前目录下创建子文件夹，最后生成文件保存在该文件夹下
username=""                                  #用户名
password=""                                  #密码
course="2145cea6801d48d3be2114bec400bfde"    #找到自己的课程名，复制地址 http://pkupc.cn/programming/course/(将这一部分粘贴到引号中)/show.do
d="pkupc.cn"                                 #长时间无响应可试试改为"162.105.86.11"或"162.105.86.10"

#------必读部分   end------

pond=["pkupc.cn/programming","162.105.86.11/programming","162.105.86.10/programming"]
if __name__=="__main__":
    import path1

    cl = path1.getcon(course, d)
    for con in cl:
        filename = name + con
        cookie = path1.login(username, password, con, course, d)
        path1.pkupc(con, cookie, filename, course, d)
    import makepage

    makepage.getfile(name)

