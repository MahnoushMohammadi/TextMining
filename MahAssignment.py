import collections
from nltk.corpus import stopwords
from collections import Counter

stop = stopwords.words('english')
f = open('test.txt', 'r') 
w = f.read().strip().split(" ")
words = [word for word in w if word not in stop]
t = collections.Counter(words)
for i in t.most_common():
	print i



	

		
		
		

           

	