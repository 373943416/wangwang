import nltk
text = "The quick brown fox jumpa over the lazy dog."
token = nltk.word_tokenize(text)
print(nltk.pos_tag(tokens))
