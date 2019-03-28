import pandas as pd
import gensim as gs
import warnings
import numpy as np
import math
import pickle
import os
warnings.filterwarnings('ignore')
def cosim(a,b):
    dot = np.dot(a, b)
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    cos = dot / (norma * normb)
    if math.isnan(cos):
        return -1
    else:
        return cos
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
def avvec(model,sentence):
    l=[]
    for i in sentence:
        try:
          l.append(model[i])
        except:
            print('{0} skipped shomehow'.format(i))
    if len(l)==0:
        return  [0] * 100
    else:
        k=sum(l)/len(l)
        return k
def giverec(model,kval,dict):
   # print(mod['board'])
    #print('using {0}'.format(dict.get(kval)))
    idx=[]
    dis=[]
    for k,v in dict.items():
        sentence=v.lower().split(' ')
        sentence2=dict.get(kval).lower().split(' ')
        #print(sentence)
        #print(sentence2)
        if v!=dict.get(kval):
            r=cosim(avvec(model,sentence),avvec(model,sentence2))
            idx.append(k)
            dis.append(r)
           # print('Comparing {0} with {1} distance {2}'.format(v,dict.get(kval),r))
        else:
            #print('value skipped')
            pass

    ordn=sorted(
                    list(
                        zip(
                            idx,
                            dis
                        )
                    ),
                    key=lambda x: x[1]
                )[:0:-1]
    print('resultados de acuerdo al analisis de similaridad con {0}'.format('Godfather: Part II, The (1974)'))

    return ordn

## try to make it less complicated
def createmodels():
    project_root = os.path.dirname(os.path.abspath(__file__))

    path=os.path.join(project_root, 'movies/tags.csv')
    patht=os.path.join(project_root, 'movies/movies.csv')
    print(path)
    df_words=pd.read_csv(path,usecols=['movieId','tag'],dtype={'movieId':'int32','tag':'str'})
    df_tit=pd.read_csv(patht,usecols=['movieId','title'],dtype={'movieId':'int32','tile':'str'})
    df_words=pd.merge(df_words,df_tit,on='movieId')
    #print(df_words.head())
    df_words=df_words.sort_values(by='movieId')
    #print(df_words.head())
    dict={}
    for i in df_words.values:
        #print(i)
        if i[2] not in dict:
           dict[i[2]] = i[1].lower()
        else:
            dict[i[2]] = dict.get(i[2])+' '+i[1].lower()
    #print(dict.values())
    test=df_words['tag']
    test.tolist()
    # print(len(test))
    d=''
    for i in dict.values():
        d=d+' '+i.lower()
    #print(d)
    waza=gs.utils.simple_preprocess(d)
    waza=[waza]
    #print("waza\n")
    #print(waza)
    mod=gs.models.Word2Vec(waza,size=100,
    window=5,
    min_count=1,
    workers=10)

    mod.train(waza, total_examples=len(waza), epochs=100)
    pickle.dump(mod, open('model.pkl','wb'))
    pickle.dump(dict,open('dict.dic','wb'))

# kval='Godfather: Part II, The (1974)'


