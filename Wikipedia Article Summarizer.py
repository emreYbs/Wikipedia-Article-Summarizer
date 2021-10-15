#!/bin/bash
# Install these as requirements if you need. You may also try "pip3 install beautifulsoup4" if "pip" encounters errors.
# $ pip install beautifulsoup4
# $ pip install lxml

# https://github.com/emreYbs, 3.10.2021

import bs4 as bs
import urllib.request
import re
import pyfiglet

# Normally, in Jupyter Notebooks, you may prefer to give a fixed URL, change the URL when you need it
# and not ask for user input.But I wanted to see which articles, 
# I can get a better summary and when the NLTK does "so so":)

  
welcome = pyfiglet.figlet_format("Wikipedia Article Summarizer", font = "standard" )
farewell = pyfiglet.figlet_format("Wiki", font = "doh" )
print(welcome,sep="\n\n")


userLink = input("Which Wikipedia article would you want me to summarize: ")
# Provide the Wikipedia URL like this: https://
raw_data = urllib.request.urlopen(userLink) 
document = raw_data.read()

parsed_document = bs.BeautifulSoup(document,'lxml')

article_paras = parsed_document.find_all('p')

scrapped_data = ""

for para in article_paras:
    scrapped_data += para.text

print(scrapped_data[:1500]) #You may increase or reduce the first 1000 
# or 1500 characters of the scraped text, etc

scrapped_data = re.sub(r'\[[0-9]*\]', ' ',  scrapped_data)
scrapped_data = re.sub(r'\s+', ' ',  scrapped_data)

formatted_text = re.sub('[^a-zA-Z]', ' ', scrapped_data)
formatted_text = re.sub(r'\s+', ' ', formatted_text)

import nltk #if you don't have it, then>> python3 -m pip install nltk
all_sentences = nltk.sent_tokenize(scrapped_data)

# Stop Words are the words that you will most probably ignore, so we filter them out of the text.
stopwords = nltk.corpus.stopwords.words('english')

word_freq = {}
for word in nltk.word_tokenize(formatted_text):
    if word not in stopwords:
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1

max_freq = max(word_freq.values())

for word in word_freq.keys():
    word_freq[word] = (word_freq[word]/max_freq)


sentence_scores = {}
for sentence in all_sentences:
    for token in nltk.word_tokenize(sentence.lower()):
        if token in word_freq.keys():
            if len(sentence.split(' ')) <25:
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = word_freq[token]
                else:
                    sentence_scores[sentence] += word_freq[token]


import heapq
selected_sentences= heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

text_summary = ' '.join(selected_sentences)
print(text_summary)
print(" ")
print(pyfiglet.figlet_format("                                   E.N.D", font = "standard" ))
print("\t\t\t\tEnd of Automatic summarization")
print(farewell + "\t\t\tWikipedia Article Summarizer by EmreYbs")
print("\t\t\t\tHope you liked my summary",sep="  ")