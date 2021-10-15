# Wikipedia-Article-Summarizer

a simple Python project based on NLP techniques

Text Summarization with NLTK
*(NLTK, or Natural Language Toolkit, is a Python package that you can use for NLP tasks

*Note: I've exported this Jupyter Notebook as pdf in case you may not Jupyter installed or not use Visual Stuido Code. In the repo, you can check the pdf version for convenience.*


![image](https://user-images.githubusercontent.com/59505246/137485419-7530cd8e-8ce2-46e6-945b-29f84614b2d2.png)


![image](https://user-images.githubusercontent.com/59505246/137485619-b5330b5d-2450-400a-bc1a-a6d817508ed7.png)


![image](https://user-images.githubusercontent.com/59505246/137485727-454cb2d9-af82-45a1-9d39-892fa2a26d6e.png)

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
