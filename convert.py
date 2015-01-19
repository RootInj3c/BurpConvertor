from xml.dom import minidom
import base64,sys

if len(sys.argv) > 1:
    filename = str(sys.argv[1])
    fnewHTML = filename + "-Report.html"
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('item')
    fHandler = open(fnewHTML.replace(".xml",""),"w+")

    def getText(nodelist):
        rc = []
        for node in nodelist:
                rc.append(node.data)
        return ''.join(rc)

    fHandler.write("<!--Create By Maor Tal--><H1>Report Burp Requests</h1>")
    for Item in range(0,len(itemlist)):
        Current = itemlist[Item]
        fHandler.write("<hr>")
        fHandler.write("<h1>Request:</h1>"+base64.b64decode(getText(Current.getElementsByTagName('request')[0].childNodes)).replace("\n","<br>"))
        fHandler.write("<h1>Response:</h1>"+base64.b64decode(getText(Current.getElementsByTagName('response')[0].childNodes)).replace("\n","<br>"))

    fHandler.close()
else:
    print "Format: convert.py <filename.xml>"

