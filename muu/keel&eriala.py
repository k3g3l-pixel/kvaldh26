python -m spacy download de_core_news_sm
import spacy
nlp = spacy.load("de_core_news_sm")
import de_core_news_sm
nlp = de_core_news_sm.load()
doc = nlp("Dies ist ein Satz.")
print([(w.text, w.pos_) for w in doc])
