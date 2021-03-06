print("开始------------------------")

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import time
from tqdm import tqdm

def reader_pandas(file, chunkSize=100000, patitions=10 ** 4):
    reader = pd.read_csv(file, iterator=True)
    chunks = []
    with tqdm(range(patitions), 'Reading ...') as t:
        for _ in t:
            try:
                chunk = reader.get_chunk(chunkSize)
                chunks.append(chunk)
            except StopIteration:
                break
    return pd.concat(chunks, ignore_index=True)


print("开始读入数据")
tic=time.time()
# df_train=pd.read_csv('./train_set.csv')
# df_test=pd.read_csv('./test_set.csv')
df_train=reader_pandas('./train_set.csv')
df_test=reader_pandas('./test_set.csv')
df_train.drop(columns=['article','id'],inplace=True)
df_test.drop(columns=['article'],inplace=True)
toc=time.time()
print("读入完毕，耗时"+str(toc-tic)+"s")

print("开始进行数据预处理")
tic=time.time()
vectorizer=CountVectorizer(ngram_range=(1,2),min_df=3,max_df=0.9,max_features=100000)
vectorizer.fit(df_train['word_seg'])
x_train=vectorizer.transform(df_train['word_seg'])
x_test=vectorizer.transform(df_test['word_seg'])
y_train=df_train['class']-1
toc=time.time()
print("数据预处理完毕，耗时"+str(toc-tic)+"s")

print("开始训练")
tic=time.time()
lg=LogisticRegression(C=4,dual=True)
lg.fit(x_train,y_train)
toc=time.time()
print("训练完毕，耗时"+str(toc-tic)+"s")

print("开始生成预测数据")
tic=time.time()
y_test=lg.predict(x_test)
toc=time.time()
print("预测数据生成完毕，耗时"+str(toc-tic)+"s")

print("开始保存结果到本地")
tic=time.time()
df_test['class']=y_test.tolist()
df_test['class']=df_test['class']+1
df_result=df_test.loc[:,['id','class']]
df_result.to_csv('./result.csv',index=False)
toc=time.time()
print("结果保存完毕，耗时"+str(toc-tic)+"s")

print("完成------------------------")

# df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
#                     'mask': ['red', 'purple'],
#                  'weapon': ['sai', 'bo staff']})
# df.to_csv('./result.csv',index=False)


