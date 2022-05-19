# Wikipedia-Article-Summarizer
# **(_Text Summarization with NLTK_ )** #

A simple Python project based on NLP techniques: You provide a Wikipedia Article and later get the summary.


![image](https://user-images.githubusercontent.com/59505246/137501279-73ddf768-ff57-407b-853b-b6acd0422907.png)

*Note: I've exported this Jupyter Notebook as pdf in case you may not Jupyter installed or not use Visual Stuido Code. In the repo, you can check the pdf version for convenience. Or use the python version*

**STEPS:** When you run the Wikipedia Article Summarizer.py, or use the Jupyter Notebook version,                                                            

1. The python code will ask you to provide the URL address of the Wikipedia Article, *-in English Articles-* </br>
                        *Which Wikipedia article would you want me to summarize? : (URL)*
                        
                        *Provide the Wikipedia URL like this: ( https://    )*

2. The article you have provided will be summarized via Natural Language Processing techniques.

**Note:** I use my bash scripts and provide some Wikipedia article links and get short summarization of the links I gave. Time-saving for a student or who reads articles a lot in Wikipedia.

**EXAMPLE URL:** I have given a short article, but if you provide a long article, the code will perform better. Since I wanted to add some screenshots, I kept it short. https://en.wikipedia.org/wiki/Aalto_University_School_of_Science_and_Technology

https://en.wikipedia.org/wiki/F-Secure  (You can see the code in action with Short Articles)</br>
https://en.wikipedia.org/wiki/Sufism  (This article is longer and the longer the better, well, generally, for the summary:)

Try with many different Wikipedia Articles in English to test the code. For now, I am happy and improving the code and making it more complex is beyond my current skills:), but you are free to fork and improve it.


![image](https://user-images.githubusercontent.com/59505246/137502335-5b2096b0-05c1-44f5-a341-afdf5ed23868.png)

![image](https://user-images.githubusercontent.com/59505246/137500999-d8215f8d-ee93-4b30-830e-f017f2d2219b.png)


![image](https://user-images.githubusercontent.com/59505246/137485419-7530cd8e-8ce2-46e6-945b-29f84614b2d2.png)


![image](https://user-images.githubusercontent.com/59505246/137485619-b5330b5d-2450-400a-bc1a-a6d817508ed7.png)


![image](https://user-images.githubusercontent.com/59505246/137485727-454cb2d9-af82-45a1-9d39-892fa2a26d6e.png)

 **Requirements**

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

**Example:**<br /> 
raw_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/F-Secure')  (*with a pre-given Wikipedia URL*) <br /> 
document = raw_data.read()

*Since I like F-Secure and wishing to attend their trainings, I search for them and wrote this this simple Wikipedia Article summarizer to practise NLP and Python, meanwhile learning more about F-Secure, its history, culture, etc.*

![image](https://user-images.githubusercontent.com/59505246/137503439-45135716-7b14-4d0f-9972-c37abc59cf4d.png)



