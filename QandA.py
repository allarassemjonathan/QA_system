import spacy as s
# Load dataset
model = s.load("en_core_web_md")

# Configure sentencizer
config = {"punct_chars": None}
model.add_pipe("sentencizer", config=config)

content = open("Knowledge_Source.txt","r", encoding="utf8").read(1000000)
# model.max_length = len(content) + 100
history_doc = model(content, disable = ["ner", "parser"])

q = ""
while(q != "Quit"):
    q = input("Ask me a question...(type 'Quit' to quit)")
    if q == "Quit":
        break
    to_remove = set()
    for w in model(q):
        if w.is_punct or w.is_space or w.is_stop:
            to_remove.add(w.text)
            
    for e in to_remove:
        q = q.replace(e,"")
    
    question = model(q)
    print(question.text)
    max_sim = 0
    answer = None
    for sentence in history_doc.sents:
        cur_sim = sentence.similarity(question)
        if cur_sim > max_sim:
            max_sim = cur_sim
            answer = sentence
    print(answer)
