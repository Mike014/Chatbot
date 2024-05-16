import re
import nltk
from nltk.corpus import gutenberg

nltk.download('treebank')
nltk.download('gutenberg')

word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)  # Output: ['u', 'e', 'a', 'i', 'a', 'i', 'i', 'i', 'e', 'i', 'a', 'i', 'o', 'i', 'o', 'u']
len(re.findall(r'[aeiou]', word))  # Output: 16

wsj = sorted(set(nltk.corpus.treebank.words()))# nltk.corpus.treebank.words() returns a list of words in the treebank corpus
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))# FreqDist is a class that counts the frequency of each item in the list
print(fd.most_common(12))  # Output: [('io', 549), ('ea', 476), ('ie', 331), ('ou', 329), ('ai', 261), ('ia', 253), ('ee', 217), ('oo', 174), ('ua', 109), ('au', 106), ('ue', 105), ('ui', 95)]

[int(n) for n in re.findall(r'\d+', '2009-12-31')]  # Output: [2009, 12, 31]

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r"<a> (<.*>) <man>")

text = "That U.S.A. poster-print cost $12.40..."

pattern = r'''(?x)     # set flag to allow verbose regexps
    (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
  | \w+(?:-\w+)*       # words with optional internal hyphens
  | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
  | \.\.\.             # ellipsis
  | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''

tokens = nltk.regexp_tokenize(text, pattern)

print(tokens)

text2 = "Goodmorning! Today it's a beautiful day. Let's have a walk"

sentences = nltk.sent_tokenize(text2)

for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")
    



  




