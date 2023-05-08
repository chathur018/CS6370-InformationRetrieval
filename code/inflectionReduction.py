from util import *

# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None

		#Fill in code here

		lemmatizer = nltk.WordNetLemmatizer()
		
		reducedText = []
		for s in text:
			tempSentence = []
			for w in s:
				tempSentence.append(lemmatizer.lemmatize(w))
			reducedText.append(tempSentence)
		
		return reducedText


