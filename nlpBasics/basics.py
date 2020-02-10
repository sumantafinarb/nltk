import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Speaker 1:  Thank you for calling Winnetka Pharmacy. This is Vicky speaking. Can I help you? . Speaker 2: You know what your fax number there? . Speaker 1: It is a doctors office. . Speaker 2: No, no. . Speaker 1: Its 7:47. 9000 8489 . Speaker 2: Hope youre so you. Dont use fax number 564-4495 any more of it. now Okay. Alright. Thank you.')

for token in doc:
    print(token.text,token.pos,token.pos_,token.dep_)


for token in doc.noun_chunks:
    print(token)

nlp.pipeline
nlp.pipe_names

# tokenization
# spliting all the part in token

myString = 'we\'re moving to la'

from spacy import displacy


displacy.render(doc,style='ent')