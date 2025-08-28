import numpy as np

class ngrams():
    def __init__(self,N,corpus,data=[]):
        self.N=N
        self.corpus=corpus
        self.data=data
        
    def defineData(self):
        self.corpus.lower()
        self.corpus.replace('!','').replace('.','').replace('?','').replace('"','').replace(',','').replace(';','').replace('(','').replace(')','')
        self.data=self.corpus.split(' ')
        self.data=[item.strip for item in self.data]
        self.data=np.array(self.data)
    
    def findWords(self,word):
        wordsAfter=[]
        indices = np.array(np.where(self.data == word)[0])
        for i in indices:
            wordsAfter.append(self.data[i+1])
        return wordsAfter