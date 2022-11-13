import requests 
from bs4 import BeautifulSoup 
from transformers import pipeline 

link = "https://www.geeksforgeeks.org/how-to-scrape-paragraphs-using-python/" 
f = requests.get(link) 

soup = BeautifulSoup(f.text, features = "html.parser") 
tags = soup.find_all("p") #find a way to target multiple tags and convert them into text while still filtering out the content
context = ''

for data in tags:
    context = context + data.get_text()

print (context)

question_answering = pipeline ("question-answering")
context = "Hominin expansion from Africa is estimated to have reached the Indian subcontinent approximately two million years ago, and possibly as early as 2.2 million years before the present.[32][33][34] This dating is based on the known presence of Homo erectus in Indonesia by 1.8 million years before the present and in East Asia by 1.36 million years before present, as well as the discovery of stone tools at Riwat in the Soan River valley of the Pabbi Hills region, Pakistan.[33][35] Although some older discoveries have been claimed, the suggested dates, based on the dating of fluvial sediments, have not been independently verified.[34][36]The oldest hominin fossil remains in the Indian subcontinent are those of Homo erectus or Homo heidelbergensis, from the Narmada Valley in central India, and are dated to approximately half a million years ago.[33][36] Older fossil finds have been claimed, but are considered unreliable.[36] Reviews of archaeological evidence have suggested that occupation of the Indian subcontinent by hominins was sporadic until approximately 700,000 years ago, and was geographically widespread by approximately 250,000 years before the present, from which point onward, archaeological evidence of proto-human presence is widely mentioned.[36][34]According to a historical demographer of South Asia, Tim Dyson:"
while True:
    question = input ("user: ")
    result = question_answering(question = question, context = context)
    print ("Answer: ", result['answer'])