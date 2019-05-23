import os
import re

rootdir=r'C:\Users\lenovo\Desktop\NLP\IR_PROJECT\PROJECT 1\属性抽取\Project_Data'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir, list[i])
    print(list[i])
    with open(path,'r',encoding='utf-8') as f:
        text=f.read()
        # print(type(text))
        # print(text)
        # sentences=text.split('##。.,，、；;--:：  ')
        sentences=text.split()
        for sentence in sentences:
            if ("start" in sentence or "end" in sentence or "---" in sentence):
                continue
            print(sentence)
        print(sentences.__sizeof__())
        matchObj=re.search(r'.?.?.?.?.?.?.?.?.?.?.?周岁.?.?.?.?.?.?.?.?',text,flags=0)
        print(type(matchObj))
        if matchObj:
            print(matchObj.group())
        # print(matchObj.group())
        else:
            print("Nothing found")
    break


# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# print(type(matchObj))
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) :" , matchObj.group(2))
# else:
#     print("No match!!")
