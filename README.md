# Wikipedia-Article-Summarizer

a simple Python project based on NLP techniques

Text Summarization with NLTK
*(NLTK, or Natural Language Toolkit, is a Python package that you can use for NLP tasks

# Requirements

 Install these as requirements if you need. You may also try "pip3 install beautifulsoup4" if "pip" encounters errors.
 
  pip install beautifulsoup4 <br /> 
  pip install lxml <br /> 
  pip install nltk  (you may also need to install stopwords package)


# NOTES:

**Normally, in Jupyter Notebooks, you may prefer to give a fixed URL, change the URL when you need it
and not ask for user input. But I wanted to see from which
articles I can get a better summary and when the NLTK does "so so":)** *That's why, I ask for user input and give different Wikipedia articles in English language. Also, this way, code is more flexible.*

userLink = input("Which Wikipedia article would you want me to summarize: ")  #with user input version, a bit more flexible


#If you prefer a fixed URL in the code or if you encounter an error in Jupyter, then you can also change the code with a pre-given URL and change accordingly later in Jupyter Notebook.

*Example:*<br /> 
raw_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/F-Secure')  (*with a pre-given Wikipedia URL*) <br /> 
document = raw_data.read()

*Since I like F-Secure and wishing to attend their trainings, I search for them and wrote this this simple Wikipedia Article summarizer to practise NLP and Python, meanwhile learning more about F-Secure, its history, culture, etc.*


*Provide the Wikipedia URL like this: ( https://    )*
