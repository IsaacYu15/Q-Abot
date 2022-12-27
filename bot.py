import requests 
from bs4 import BeautifulSoup 
#from transformers import pipeline 

link = "https://www.w3schools.com/python/ref_func_print.asp#:~:text=The%20print()%20function%20prints,before%20written%20to%20the%20screen." 
f = requests.get(link) 

soup = BeautifulSoup(f.text, features = "html.parser") 

for link in soup.find_all("a"):
    link.decompose()

context = soup.get_text().replace('\n', ' ')
print (context)

question_answering = pipeline ("question-answering")
while True:
   question = input ("user: ")
   result = question_answering(question = question, context = context)
   print ("Answer: ", result['answer'])