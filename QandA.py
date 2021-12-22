import spacy as sp

#Loading the model 
nlp = sp.load("en_core_web_lg")

#Ask a question
inp = nlp(input('Question your past!'))

#Loading the text
f = open(r"C:\Users\ALLARASSEMJJ20\QA_system\Knowledge_Source.txt", encoding="utf-8")
text = f.read(500000)

#Cleaning the text
text = text.replace("\n", "")
text = text.replace("— ", "")
text = text.replace("- ", "")


#adding the sentencizer
nlp.add_pipe("sentencizer")

#Applying it to the text
doc = nlp(text)

#Naive approach. The max similarity is the answer
maxi = 0
answer = ''
for i in doc.sents:
    if(maxi < i.similarity(inp)):
        answer = i
        maxi = i.similarity(inp)

print(answer)

