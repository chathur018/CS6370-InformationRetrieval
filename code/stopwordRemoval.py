from util import *

# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None

		#Fill in code here

		nltkStopWords = set(nltk.corpus.stopwords.words("english"))
		
		stopwordRemovedText = []
		for s in text:
			tempSentence = []
			for w in s:
				if not w.lower() in nltkStopWords:
					tempSentence.append(w)
			stopwordRemovedText.append(tempSentence)


		return stopwordRemovedText




	