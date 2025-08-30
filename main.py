from binascii import Error
import numpy as np
import re
from collections import defaultdict, Counter
import random
import PyPDF2
from time import sleep

class Ngram():

  def __init__(self,corpus,maxlength,N=2,data=[]):
    self.corpus=corpus
    self.maxlength=maxlength
    self.N=N
    self.data=data
    self.model=defaultdict(list)

  def treatData(self):
    self.corpus=self.corpus.lower()
    self.corpus=re.sub(r"[^a-zA-ZÀ-ÿ\s]","",self.corpus)
    self.data=[item.strip() for item in self.corpus.split(' ') if item.strip() != ""]
    self.data=np.array(self.data)

    for i in range(len(self.data) - self.N+1):
      key=tuple(self.data[i:i+self.N-1])
      next_word=self.data[i+self.N-1]
      self.model[key].append(next_word)

  def findWord(self, context):
    if context not in self.model:
      return random.choice(self.data)

    counter=Counter(self.model[context])
    return random.choices(list(counter.keys()),weights=counter.values())[0]

  def runModel(self):
    self.maxlength = int(input('Input the max length: '))
    firstWords = input(f'Input the first {self.N-1} word(s): ').split()

    if len(firstWords)<self.N-1:
      raise Error(f"You must input atleast {self.N-1} initial word(s).")

    context=tuple(firstWords[-(self.N-1):])
    sentence=list(firstWords)

    while len(sentence)<self.maxlength:
      next_word=self.findWord(context)
      sentence.append(next_word)
      context=tuple(sentence[-(self.N-1):])
      print(" ".join(sentence), end="\n")
      sleep(0.1)

    return " ".join(sentence)

  def getFullText(self, results):
    fullText=''
    for letter in results:
      if letter!="\n":
        fullText+=letter
      else:
        fullText+=" "
    return fullText

def defineData(path):
  text=""
  with open(path, "rb") as pdffile:
    reader = PyPDF2.PdfReader(pdffile)
    for page in reader.pages:
      text += page.extract_text() + " "
  return text

model=Ngram(defineData("ua00106a.pdf"), None, N=int(input("Input the target N of the N-grams model. "))+1)
model.treatData()

print("\n\n-=- Full text -=-\n\n", model.getFullText(model.runModel()))
