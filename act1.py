from tabulate import tabulate
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
def test(d):
  return max(d, key = d.get)

statement = input("Enter the Statement")
words_number = len(statement.split())
words = []
words = statement.split()
wfreq=[words.count(w) for w in words]
freq = dict(zip(words,wfreq))
frequency = test(freq)
number_of_sentences = sent_tokenize(statement)
number = len(number_of_sentences)
data = [["Answer",words_number,number,frequency]]
print (tabulate(data, headers=["No. of words", "No. of Statements", "Most frequent word in the paragraph"]))
