import spacy as sp
import numpy as np
import matplotlib.pyplot as plt

#Loading the model containing vocabulary
nlp = sp.load("en_core_web_lg")

#Ask a question
q = input('Question your past!')
inp = nlp(q)
nw = ''
punc = ['What','Who', 'Where', 'When', 'How']
for e in inp:
    if e.is_stop and e.text not in punc:
        pass
    elif e.text in punc:
        if e.text == 'What':
            nw+='thing' + ''
        elif e.text == 'Who':
            nw+='person' + ' '
        elif e.text == 'Where':
            nw+='map' + ' '
        elif e.text == 'When':
            nw+='time' + ' '
    else:
        nw+=e.text + ' '
        
inp = nlp(nw)
print(inp)

#Loading the text
f = open(r"C:\Users\ALLARASSEMJJ20\QA_system\wiki_test_second.txt", encoding="utf-8")
text = f.read()

#Cleaning the text

#adding the sentencizer
nlp.add_pipe("sentencizer")

#Applying it to the text
doc = nlp(text)

#Naive approach. The max similarity is the answer
maxi = 0
sim = 0
answer = ''
arr = np.array([])
for i in doc.sents:
    print(i)
    print(i.similarity(inp))
    arr = np.append(arr, i.similarity(inp))
    if(maxi < i.similarity(inp)):
        answer = i
        maxi = i.similarity(inp)

print(answer)
plt.title('plot' + q+ str(np.std(arr)) + ' ' +str(maxi))
print(arr)
index = np.array([x for x in range(len(arr))])
plt.scatter(index, arr)
plt.show()

    



