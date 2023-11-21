#import the packages
from newspaper import Article
import string
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from time import sleep as sl
import random as rd
from bs4 import BeautifulSoup
import requests

warnings.filterwarnings('ignore')

nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)


def dontknow(query):
    print(query)

def teach(url, query):
    article= Article(url)
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    sent_tokens=nltk.sent_tokenize(text)
    remove_punct_dict=dict( (ord(punct),None) for punct in string.punctuation)
    def LemNormalize(text):
        return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
    def response(user_response):
        user_response=user_response.lower()
        robo_response=''
        sent_tokens.append(user_response)
        tfidfvec=TfidfVectorizer(tokenizer=LemNormalize , stop_words='english')
        tfidf=tfidfvec.fit_transform(sent_tokens)
        val=cosine_similarity(tfidf[-1],tfidf)
        idx=val.argsort()[0][-2]
        flat=val.flatten()
        flat.sort()
        score=flat[-2]
        if score==0:
            dontknow(f"We didn't understand your query... Please try again later...")
        else:
            robo_response=robo_response+sent_tokens[idx]
        sent_tokens.remove(user_response)
        return robo_response
    sl(rd.randrange(5,13))
    print(response(query))

def ext(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    allData = soup.find_all("div",{"class":"g"})
    g=0
    Data = [ ]
    l={}
    for i in range(0,len(allData)):
        link = allData[i].find('a').get('href')
        if(link is not None):
            if(link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
                g=g+1
                l["link"]=link
                Data.append(l)
                l={}
            else:
                continue
        else:
            continue 
    with open("./tmp_knobedx/doubt.knobedx", '+a') as f:
        f.writelines(Data[0]['link']+'\n')

def url(classs, sylab, chap, subject):
	sen = f'class {classs} {sylab} notes for {subject} chapter {chap} from learn cbse'
	ext(f"https://www.google.com/search?q={sen}")

def doubt(classs, sylab, chap, sub):
    print(" ")
    print("Beware... The product is an Experimental feature... The results maybe inaccurate... Please bear with us...")
    sl(rd.randrange(2,5))
    query = input("Enter your question: ")
    url(classs, sylab, chap, sub)
    with open("./tmp_knobedx/doubt.knobedx") as f:
        lt = f.readlines()
        link = lt[-1]
    teach(link, query)