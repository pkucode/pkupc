#！请不要运行本程序，请运行main.py!#

info={"Author":"https://github.com/pkucode",
"Name":"pkupc题目及代码自动抓取器",
"CurrentFile":"makepage.py",
"Function":"创建一个网页，可以把抓取的题目的链接整合到网页上"}
def makesite(tmp,filename):


    begin = """
    <!doctype html>
     <html lang="zh">
     <head>
     <meta charset="UTF-8">
     <title>pkucode@github.com</title>
     </head>
     <body leftmargin="20" topmargin="20" marginwidth="20" marginheight="20" >
    <div class="mainContext">
    <div style="width:50%;float:left;height:100%">"""

    middle = """</div>

    <div style="width:50%;float:left;height:100%">"""

    end = """</div>
    </div>
     </body>

     </html>"""
    affair = tmp
    row1, row2 = "", ""
    for n in affair:
        row1 += '<a fontsize="20" href="' + affair[n] + '">' + n + '</a><br>'
    al = begin + row1 + middle + row2 + end
    rfile = open(filename+".html", "w")
    print(al, file=rfile)
    rfile.close()

def walkdire(file):
    import os
    def walkFile(file):
        for root, dirs, files in os.walk(file):
            filename=[]
            for f in dirs:

                filename.append(f)

            return filename
    return walkFile(file)
def walkfile(file):
    import os
    def walkFile(file):
        for root, dirs, files in os.walk(file):
            filename=[]

            for f in files:

                filename.append(f)

            return filename
    return walkFile(file)
import os
di= os.path.abspath(os.path.split(__file__)[0])
directory=walkdire(di)



def getfile(info):
    filelis={}
    for n in directory:
        if info in n:
            for f in walkfile(n):
                filelis[f]=di+"/"+n+"/"+f

    makesite(filelis,info)


