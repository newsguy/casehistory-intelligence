'''
Created on May 26, 2011

@author: A.Tripathi
'''
import nltk
import urlstemmer

def getWordsFromFile(file):
    tokens = []
    try:
        raw = nltk.clean_html(file.read())
        tokens = [t.lower() for t in nltk.word_tokenize(raw) if t.isalpha()]
    except:
        print 'Error reading the file'
    return tokens

if __name__ == '__main__':
    file = open('gss.html', 'r')
    words = urlstemmer.getContentWords(getWordsFromFile(file))
    print 'words = '+str(words)
    file.close()