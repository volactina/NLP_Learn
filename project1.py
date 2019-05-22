import os
rootdir=r'C:\Users\lenovo\Desktop\NLP\IR_PROJECT\PROJECT 1\属性抽取\Project_Data'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir, list[i])
    print(list[i])
    with open(path,'r',encoding='utf-8') as f:
        text=f.read()
        print(text)
    break


