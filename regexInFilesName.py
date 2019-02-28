import os
import sys
import re
allArgv = sys.argv
if (len(allArgv) == 1 ):
    print("יש להזין נתיב, מחרוזת חיפוש, מחרוזת החלפה")
    exit()
if (len(allArgv) == 2 ):
    allArgv[2]=""
elif (os.path.isdir(allArgv[1]) != True):
    print("נתיב לא חוקי")
    exit()


reg=re.compile(""+allArgv[2]+"")
for root,dirs,files in os.walk(allArgv[1]):
    x=0;
    for file in files:
        try:
            x+=1
            temp = allArgv[3].replace("{}",str(x))
            os.rename(root+"\\"+file,root+"\\"+reg.sub(temp+"",file))
        except:
            print (sys.exc_info()[0])
