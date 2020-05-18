
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
import textstat

#convert text document into series of lines
tokenizer = RegexpTokenizer(r'\w+')
f = open("outputtext.txt", "a")
#f = open('csvfile.csv','w')
#writer = csv.writer(f, delimiter=',')
with open ('inputtext.txt') as d1:
 data = d1.read()
 phrases = sent_tokenize(data)

 for sentence in phrases:
    words = word_tokenize(sentence)
    tokens = tokenizer.tokenize(sentence)
    line = sentence+ "|"+str(len(tokens))+"|" + str(textstat.flesch_reading_ease(sentence))+"\n"
    f.writelines(line)

f.close()  
