import spacy as sp


#Loading the model 
nlp = sp.load("en_core_web_lg")

#Ask a question
q = input('Question your past!')
inp = nlp(q)

#Adding the underscores
def highlight(q):
    entities = inp.ents
    for e in entities:
        if e.text in q:
            q = q.replace(e.text, e.text.replace(' ', '_'))
    return q

#removing the underscores
def decode(entity):
    entity = entity.replace('_', ' ')
    return entity

#weighted similarity
def weights(inp):
    tokens_input = nlp(highlight(inp))
    #tokens_candidate = nlp(candidate)
    weights = []
    dumb = True
    for e in tokens_input:
        dumb = True
        for i in nlp(inp).ents:
            if i.text == decode(e.text):
                weights.append(10)
                dumb = False
        if e.is_stop:
            weights.append(1)
            dumb = False
        if dumb:
            weights.append(3)
    #sum = 0
    #i = 0
    #for c in tokens_candidate:
     #   for inpu in tokens_input:
      #      sum += weights[i]*inpu.similarity(c)
       #     i = i+1
    return weights 

def similarity(weights, question, sentence):
    

             
    
#Naive approach. The max similarity is the answer
print(similary(q))
