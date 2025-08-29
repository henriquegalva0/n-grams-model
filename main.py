from binascii import Error
import numpy as np
import re
from collections import Counter
import random
import PyPDF2
from time import sleep

class unigram():

  def __init__(self,corpus,data=[]):
    self.corpus=corpus
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


def defineData(path):
  text = ""
  with open(path, "rb") as pdffile:
    reader = PyPDF2.PdfReader(pdffile)
    for page in reader.pages:
      text += page.extract_text() + " "
  return text

model = unigram(defineData("ua00106a.pdf"),[])
model.treatData()

firstWord=input('Input the first word: ')

try:
  target=model.findWord(firstWord)
  sentence=firstWord
except:
  raise Error("This word can't be used.")

while True:
  sentence+=" "+target
  target=model.findWord(target)
  print(sentence)
  sleep(1)
