#！请不要运行本程序，请运行main.py!#

info={"Author":"https://github.com/pkucode",
"Name":"pkupc题目及代码自动抓取器",
"CurrentFile":"path1.py",
"Function":"主要功能函数"}


def getcon(course,add):
    import requests,re
    from bs4 import BeautifulSoup
    res=requests.get("http://"+add+"/programming/course/"+course+"/show.do")
    bs=BeautifulSoup(res.text,"html.parser")
    al=bs.find_all(class_="homework")[0]
    li=al.find_all("li")
    tpcon=[]
    i=0
    while(True):

        try:
            if 'color="red"' in str(li[i]):  # 修改[]中的数字可以改变抓取的作业次数，但是一定要是开放的题集，否则无效
                thecon = re.findall('problemsId=(.*?)"', str(li[i]))[0]

                tpcon.append(thecon)
                i+=1

            else:
                break

        except: break

    return tpcon

def login(username,password,content,course,add):
    header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Length': '265', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'pkupc.cn', 'Origin': 'http://'+add, 'Referer': 'http://'+add+'/programming/course/'+course+'/showProblemList.do?problemsId='+content, 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'PkupcSpider@github.com/pkucode'}
    data={
    "referer": "http://"+add+"/programming/course/"+course+"/show.do",
          "username":username,
          "password":password,
          "login":"登录"}
    import requests
    sess = requests.Session()
    res=sess.post("http://"+add+"/programming/login.do",data=data,headers=header).headers
    cookie1=sess.cookies.items()[0][1]

    return "passport="+cookie1




def pkupc(content,cookie,filename,course,add):
    import requests,re,os
    ###########
    # print(content)
    q = "http://"+add+"/programming/course/"+course+"/showProblemList.do?problemsId="

    header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive',
            'Host': add,
            'Referer': 'http://'+add+'/programming/course/'+course+'/show.do?referer=http%3A%2F%2Fpkupc.cn%2Fprogramming%2Fcourse%2F'+course+'%2Fshow.do',
            'Upgrade-Insecure-Requests': '1',
            'Cookie': cookie,

            'User-Agent': 'PkupcSpider@github.com/pkucode'}

    res=requests.get(q+content,headers=header)

    qq=re.findall("/problem/(.*?)/show.do",res.text)
    # qq=re.findall("/programming/problem/submit.history.problemId=(.*?)&problemsId=",res.text)
    # print(qq)

    os.system("mkdir "+filename)
    for f in qq:
        href="http://pkupc.cn/programming/problem/submit.history?problemId="+f+"&problemsId="+content
        quizhref = "http://"+add+"/programming/problem/"+f+"/show.do?problemsId="+content
        quizres=requests.get(quizhref,headers=header).text
        # print(quizres)
        from bs4 import BeautifulSoup
        bb = BeautifulSoup(quizres, "html.parser")
        title=bb.find_all("title")[0].get_text()
        title=title.replace("\r","").replace("\t","").replace("\n","").replace(" ","").replace(".","").replace("(","").replace(")","")

        m=quizres.find("</body>")
        st=quizres[:m]
        en=quizres[m:]
        try:
            # 抓取提交记录
            res2 = requests.get(href, headers=header)
            source = res2.text
            targe = re.findall("solution.do.solutionId=(.*?)&sourceCode=true", source)
            count = 1
            for t in targe:
                target = "http://"+add+"/programming/problem/solution.do?solutionId=" + t + "&sourceCode=true"
                res3 = requests.get(target, headers=header)
                so = res3.text
                from bs4 import BeautifulSoup
                bs = BeautifulSoup(so, "html.parser")
                try:
                    ac = bs.find_all(color="blue")[0]
                except:
                    ac = bs.find_all(color="red")[0]
                st = st + '<br><br><font size="15">' + ac.get_text() + "</font><br><br>"
                st = st + "<br><pre>" + str(bs.find_all("code")[0]) + "</pre><br><br><br>"
                count += 1
        except:pass
        print("成功抓取题目'"+title+"',正在合成网页")
        rfile = open(filename+"/" + title + ".html", "w", encoding="gb2312")
        print(st+en, file=rfile)


