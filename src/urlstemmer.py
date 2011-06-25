import nltk
from urllib import urlopen

def urlStemmer(url):
	raw = nltk.clean_html(urlopen(url).read())
	tokens = nltk.word_tokenize(raw)
	print 'Number of tokens = '+str(len(tokens))
	print 'performing stemming on the text from '+url
	porter = nltk.PorterStemmer()
	porterstems = [porter.stem(t).lower() for t in tokens]
	print 'Stemmed set size = '+str(len(porterstems))
	print 'Displaying results of Poter stemmer now:'
	print porterstems
	lancaster = nltk.LancasterStemmer()
	lancasterstems = [lancaster.stem(t).lower() for t in tokens]
	print 'Stemmed set size = '+str(len(lancasterstems))
	print 'Displaying results of Lancaster stemmer now:'
	print lancasterstems

	
def getWordsFromUrl(url):
	porterstems = []
	try:
		raw = nltk.clean_html(urlopen(url).read())
		tokens = nltk.word_tokenize(raw)
		porter = nltk.PorterStemmer()
		porterstems = [porter.stem(t).lower() for t in tokens]
	except:
		print 'Error opening the url: '+url
		print 'Exiting gracefully ...'
	return porterstems

def formDoc(url, category):
	document = (list(getWordsFromUrl(url)), category)
	return document

def wordFeatures(words):
	all_words = nltk.FreqDist(w.lower() for w in words)
	word_features = all_words.keys()
	return word_features

def documentFeatures(words, word_features):
	document_words = set(words)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
''' print document_features(movie_reviews.words('pos/cv957_8737.txt')) '''
	
def train(documents, word_features):
	featuresets = [(documentFeatures(d, word_features), c) for (d,c) in documents]
	classifier = nltk.NaiveBayesClassifier.train(featuresets)
	return classifier
	''' find a better way to do this '''

if __name__ == '__main__':
	print 'Starting to train the classifier ...'
	words1 = getWordsFromUrl('http://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered')
	print 'words1 done'
	words2 = getWordsFromUrl('http://stackoverflow.com/questions/5519513/erlang-like-concurrency-for-python')
	print 'words2 done'
	words3 = getWordsFromUrl('http://www.imdb.com/title/tt0443453/quotes')
	print 'words3 done'
	words4 = getWordsFromUrl('http://www.nytimes.com/pages/nyregion/index.html')
	print 'words4 done'
	words5 = getWordsFromUrl('http://www.dnipogo.org/fcs/def_power_games_98.htm')
	print 'words5 done'
	words6 = getWordsFromUrl('http://serendipity.caplin.com/2010/07/06/ion-buys-lab49-2/')
	print 'words6 done'
	words7 = getWordsFromUrl('http://jeremymanson.blogspot.com/2010/07/why-many-profilers-have-serious.html')
	print 'words7 done'
	doc1 = (list(words1), 'Programming')
	doc2 = (list(words2), 'Programming')
	doc3 = (list(words3), 'Programming')
	doc4 = (list(words4), 'Programming')
	doc5 = (list(words5), 'Programming')
	doc6 = (list(words6), 'Programming')
	doc7 = (list(words7), 'Programming')
	words = words1+words2+words3+words4+words5+words6+words7
	word_features = wordFeatures(words)
	doclist = [doc1, doc2, doc3, doc4, doc5, doc6, doc7]
	classifier = train(doclist, word_features)
	print 'Classifier trained, will classify the inputs now ...'
	file = open('feedlist.txt', 'r')
	result = open('classified.txt', 'w')
	for url in file:
		print 'Classifying '+url
		result.write(url+' : '+classifier.classify(documentFeatures(list(getWordsFromUrl(url)), word_features))+'\n')
	file.close()
	result.close()
	'''print classifier.classify(documentFeatures(list(getWordsFromUrl('http://diveintopython3.org/your-first-python-program.html')), word_features))
	print classifier.classify(documentFeatures(list(getWordsFromUrl('http://jeremymanson.blogspot.com/2010/07/why-many-profilers-have-serious.html')), word_features))
	print classifier.classify(documentFeatures(list(getWordsFromUrl('http://today.java.net/pub/a/today/2006/01/10/introduction-to-nutch-1.html')), word_features))
	print(urlstemmer('http://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered'))'''
    
