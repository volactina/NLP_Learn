# NLP_Learn
本项目代码为深度之眼训练营（CS224N-NLP）的代码记录

Day 2  

资源 https://pan.baidu.com/s/1D6H6aYEOn75C0pzy2fKgoA   提取码：lwj4

“达观杯”文本智能处理挑战赛的代码，比赛数据集存储在百度云

发生错误pandas.errors.ParserError: Error tokenizing data. C error: out of memory

疑似原因https://blog.csdn.net/leiting_imecas/article/details/68928553

疑似解决方案https://blog.csdn.net/susannusas/article/details/79875209

在windows下载了https://download.csdn.net/download/qq1084502122/10734836

转换后依然失败，下一步在linux服务器上尝试（更大的内存）

尝试通过以下方法在ubuntu上下载存在百度云里的数据集

https://blog.csdn.net/feifanhanmc/article/details/82819425

由于无法按博客指示的直接在chrome中搜索到BaiduExporter，因此直接下载插件并加入到chrome中(注意要使用博客中指出的github上的baiduexporter项目上下载的最新版插件才能成功显示出能够导出aria2代码的按钮）

最终上述方法未能成功，改为直接从本地上传文件至服务器，但是使用SCP命令依然无法成功（可能时因为windows下没有安装Openssh插件？），最后使用WinSCP工具成功上传。
