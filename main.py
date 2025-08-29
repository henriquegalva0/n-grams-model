from binascii import Error
import numpy as np
import re
from collections import Counter
import random
import PyPDF2
from time import sleep

class unigram():

  def __init__(self,corpus,maxlength,data=[]):
    self.corpus=corpus
    self.maxlength=maxlength
    self.data=data

  def treatData(self):
    self.corpus = self.corpus.lower()
    self.corpus=re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", self.corpus)
    self.data=self.corpus.split(' ')
    self.data = [item.strip() for item in self.data if item.strip() != ""]
    self.data=np.array(self.data)
  
  def findWord(self,targetWord):
    wordsAfter=[]
    indices = np.array(np.where(self.data == targetWord)[0])

    for i in indices:
      if i + 1 < len(self.data):
        wordsAfter.append(self.data[i+1])
    
    highest_freq = max(Counter(wordsAfter).values())
    most_frequent = [item for item, freq in Counter(wordsAfter).items() if freq == highest_freq]

    return random.choice(most_frequent)
  
  def findWord(self, targetWord):
    wordsAfter = []
    indices = np.where(self.data == targetWord)[0]

    for i in indices:
      if i + 1 < len(self.data):
        wordsAfter.append(self.data[i+1])

    if not wordsAfter:
      return random.choice(self.data)

    counter = Counter(wordsAfter)
    return random.choices(list(counter.keys()), weights=counter.values())[0]
  
  def runModel(self):
    self.maxlength=int(input('Input the max length: '))
    firstWord=str(input('Input the first word: '))
    target=self.findWord(firstWord)
    sentence=firstWord

    while len(sentence)<self.maxlength:
      sentence+=" "+target
      target=model.findWord(target)
      print(sentence,end="\n")
      sleep(0.2)
    return str(sentence)

  def getFullText(self,results):
    fullText=''
    for letter in results:
      if letter != "\n":
        fullText+=letter
      else:
        fullText+=" "
    return fullText

def defineData(path):
  text = ""
  with open(path, "rb") as pdffile:
    reader = PyPDF2.PdfReader(pdffile)
    for page in reader.pages:
      text += page.extract_text() + " "
  return text

model = unigram(defineData("ua00106a.pdf"),200,[])
model.treatData()

print("\n\n-=- Full text -=-\n\n",model.getFullText(model.runModel()))
