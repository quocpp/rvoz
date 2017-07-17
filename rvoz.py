#!/usr/bin/python2
from lxml import html
import requests
import re
BeginFirstPost = "<!-- END TEMPLATE: ad_showthread_firstpost_start -->"
BeginMes =  "<!-- message -->"
EndMes = "<!-- / message -->"
def showbox(link):
    pcount = 1
    link1 = link;

    while (1):
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
 
        try:
            print link1
            page = requests.get(link1)
            tree = html.fromstring(page.content)
        except:
            return ""
        
        match = re.findall(r'thread_title.*.>(.*)<\/a>', page.content)
        match1 = re.findall(r'<a href="(.*)" id', page.content)
        for idx, item in enumerate(match):
            print "["+str(idx)+"]"+" "+item
        match2 = re.findall(r'>(Page.*.of.*.)<',page.content)
        if(len(match2) >0):
            print match2[0]

        #nb = input('Choose a number: ')
        nb = raw_input('n: Next, b: Back, g: goto, number: select: ')
        print nb
        if nb is "n":
            pcount = pcount + 1
        elif nb is "b":
            pcount = pcount - 1
        elif nb is "g":
            nb = raw_input('Input number: ')
            pcount = int(nb)
        elif nb is "r":
            pcount = pcount
        else:
            #return match1[nb]
            gettopic("https://vozforums.com/"+match1[int(nb)])
        link1 = link+"&order=desc&page="+str(pcount)

def gettopic(link1):
#    try:
    pcount = 1
    link = link1
    while(1):
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        BFP = 0;
        BBP = 0;
        print link
        page = requests.get(link)
        tree = html.fromstring(page.content)
        pageconten = re.sub(r'-->','-->\n',page.content)
        #for item in page.content.split(b'\n'):
        for item in pageconten.split(b'\n'):
            match = re.findall(r'>(Page.*.of.*.)<',item.strip())
            if(len(match) >0):
                print match[0]
            match = re.findall(r'bigusername.*">(.*)<\/a>',item.strip())
            if(len(match) > 0):
                print "================================================"
                print match[0]
                print ": "
            if "<!-- END TEMPLATE: bbcode_quote -->" in item:
                print "------------------------------------------------"
                continue
            if BFP == 1:
                BBP = 1;
                if EndMes in item:
                    BFP = 0;
            if BFP == 1:
                match1 = re.findall(r'^<',item.strip())
                if len(match1) <= 0:
                    line = re.sub(r"<.*\/>", "", item.strip())
                    if len(line) > 3:
                        print line
                else:
                    match2 = re.findall(r'^<.*">((?!<).*)<',item.strip())
                    if len(match2) > 0:
                        line = re.sub(r"<.*\/>", "",match2[0])
                        if len(line) > 3:
                            print line
            if BeginFirstPost in item or (BeginMes in item and BBP == 1):
                BFP = 1
        nb = raw_input('n: Next, b: Back,q: quit: select: ')
        print nb
        if nb is "n":
            pcount = pcount + 1
        elif nb is "b":
            pcount = pcount - 1
        elif nb is "g":
            nb = raw_input('Input number: ')
            pcount = int(nb)
        elif nb is "r":
            pcount = pcount
        elif nb is "q":
            return
        else:
            pcount = int(nb)
        link = link1+"&page="+str(pcount)



            
#    except:
#        return ""
file1 = open("boxlist.txt", "r")
lcount = 0
lbox = []
while (1):
    for line in file1: 
        print "["+str(lcount)+"] "+ line
        lcount = lcount + 1
        lbox.append(line)

    nb = raw_input('Choose a number: ')
    showbox(lbox[int(nb)])
#    gettopic("https://vozforums.com/"+abc)
    #gettopic("https://vozforums.com/showthread.php?t=5771925")
