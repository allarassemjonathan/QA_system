import spacy as sp
import numpy as np
import matplotlib.pyplot as plt

#Loading the model containing vocabulary
nlp = sp.load("en_core_web_lg")
model = sp.load("en_core_web_lg")

#Ask a question
q = input('Question your past!')
inp = nlp(q)
nw = ''
punc = ['What','Who', 'Where', 'When', 'How']
pts = ['.',',','?','!',')','(']
answer_type = ''
for e in inp:
    if e.is_stop and e.text not in punc:
        pass
    elif e.text in punc:
        if e.text == 'What':
            nw+='thing' + ' '
        elif e.text == 'Who':
            nw+='person' + ' '
            answer_type = 'PERSON'
        elif e.text == 'Where':
            nw+='map' + ' '
            answer_type = 'GPE'
        elif e.text == 'When':
            nw+='when' + ' '
            answer_type = 'DATE'
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

#Naive approach. 
maxi = 0
answer = ''
arr = np.array([])
arr_IR = []

#Select the sentences with the answer type in them
for i in doc.sents:
    tokens = model(i.text)
    for token in tokens.ents:
        if token.label_== answer_type or answer_type== '':
            arr_IR.append(i.text)
            break


clean = ''
nw_arr_IR = []

# Clean the sentences from random things that may mess up the results
# Removing stop words to compute the similarity afterward
for sentence in arr_IR:
    sentence = sentence.replace('\n', '')
    for n in range(100):
        val = '['+ str(n) + ']'
        sentence = sentence.replace(val, '')
    sentences = model(sentence)
    for word in sentences:
        if word.is_stop or word.text in pts:
            pass
        else:
            clean += word.text + ' '
    nw_arr_IR.append(clean)
    clean = ''

# Choose thesentence with thew highest similarity
for e in nw_arr_IR:
    index = model(e)
    arr = np.append(arr, index.similarity(inp))
    if index.similarity(inp)> maxi:
        maxi = index.similarity(inp)
        answer = index.text

print(arr_IR)
print(answer)
plt.title('plot' + q+ str(np.std(arr)) + ' ' +str(maxi))
print(arr)
index = np.array([x for x in range(len(arr))])
plt.scatter(index, arr)
plt.show()

    



