#learning how to analyze data from eyre.txt, which was scraped from internet
import nltk             #imports python package called nltk

def openFileAndGetText(filename):
    with open(filename, "r") as ourFile:    #given a filename, open it
        text=ourFile.read()                 #takes the file and reads the text. Stores it.
    return text

def cleanTokens(tokens):
    cleanWords=[]                       #initialize empty array
    for word in words:                  #for loop, iterates over array
        cleanWords.append(word.lower()) #makes each work lowercase, and adds
    return cleanWords


#print(cleanWords[0:30])

ourFile="eyre.txt"     #set variable filename as our file

text=openFileAndGetText(ourFile)
words=nltk.word_tokenize(text)       #take a long string and break it into words
cleanWords=cleanTokens(words)

print (cleanWords[0:30])
wordCounts=nltk.FreqDist(cleanWords)
#print(wordCounts.most_common(10))       #prints 10 most used words
#print(wordCounts.most_common()[-10:])  #prints ten least used words
#print(wordCounts["jane"])
#nltk.Text(cleanWords).dispersion_plot(['he','she','jane','tony'])

for word in cleanWords:
    if len(word) >= 8:
        print(word)



print(cleanWords.len(8))
