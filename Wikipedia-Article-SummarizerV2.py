#!/usr/bin/env python3
#emreYbs
# -*- coding: utf-8 -*-
# Wikipedia Article Summarizer(Wikipedia Article Summarizer.py) v.0.02
# This script uses NLTK library. The Natural Language Toolkit (NLTK) is a Python package for natural language processing.
# For further info, visit https://www.nltk.org/ and https://github.com/nltk/nltk

import urllib.request
import pip
import bs4 as bs
import lxml
import re
import heapq
import nltk  # pip install nltk
pip.main(['install', 'pyfiglet'])
import pyfiglet
import re
from time import sleep
import csv


nltk.download('punkt')
nltk.download('stopwords')



def get_article_summary(url):
    print(" ")
    raw_data = urllib.request.urlopen(url)
    document = raw_data.read()

    parsed_document = bs.BeautifulSoup(document, 'lxml')

    article_paras = parsed_document.find_all('p')

    scrapped_data = ""

    for para in article_paras:
        scrapped_data += para.text

    scrapped_data = scrapped_data[:1500]

    scrapped_data = re.sub(r'\[[0-9]*\]', ' ', scrapped_data)
    scrapped_data = re.sub(r'\s+', ' ', scrapped_data)

    formatted_text = re.sub('[^a-zA-Z]', ' ', scrapped_data)
    formatted_text = re.sub(r'\s+', ' ', formatted_text)

    all_sentences = nltk.sent_tokenize(scrapped_data)

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
        word_freq[word] = (word_freq[word] / max_freq)

    sentence_scores = {}
    for sentence in all_sentences:
        for token in nltk.word_tokenize(sentence.lower()):
            if token in word_freq.keys():
                if len(sentence.split(' ')) < 25:
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] = word_freq[token]
                    else:
                        sentence_scores[sentence] += word_freq[token]

    selected_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

    text_summary = ' '.join(selected_sentences)
    print(" ")
    return text_summary
    print(" ")

print(" ")
print("\033[94mWikipedia Article Summarizer by EmreYbs\033[0m")
sleep(1)
welcome = pyfiglet.figlet_format("Wikipedia Article Summarizer", font="standard")
farewell = pyfiglet.figlet_format("Wiki", font="doh")
print(welcome, sep="\n\n")



def verify_url(url):
    pattern = r'^https?://en\.wikipedia\.org/wiki/[\w()]+'
    if re.match(pattern, url):
        return True
    else:
        return False
 
userLink = input("\n\033[35mWhich Wikipedia article would you want me to summarize: \033[0m")
while not verify_url(userLink):
    print("Invalid URL. Please enter a valid Wikipedia URL.")
    print("Exitting...due to invalid Wikepedia URL")
    exit()
    sleep(0.5)


summary = get_article_summary(userLink) 
print(" ")
sleep(1)
print("\033[93mHere is the summary of the article you requested:\033[0m")
sleep(0.5)
print(" ")
sleep(1)
print(summary)

# Save summary as CSV file
filename = "summary.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Summary"])
    writer.writerow([summary])
    print(f"Summary saved as {filename}")
print(" ")
print(pyfiglet.figlet_format("                                   E.N.D", font="standard"))
print("\t\t\t\tEnd of Automatic summarization")
sleep(1)
print(farewell + "\t\t\tWikipedia Article Summarizer by EmreYbs")
print("\t\t\t\tHope you liked my summary\n", sep="  ")
