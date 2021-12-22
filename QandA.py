import spacy as s
# Load dataset
model = s.load("en_core_web_md")

# Configure sentencizer
config = {"punct_chars": None}
model.add_pipe("sentencizer", config=config)

content = open("Knowledge_Source.txt","r", encoding="utf8").read()
model.max_length = len(content) + 100
history_doc = model(content, disable = ["ner", "parser"])
