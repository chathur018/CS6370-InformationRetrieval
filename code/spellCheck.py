from util import *

# Add your import statements here




class SpellCheck():

	def spellCheck(self, text):
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

		spellCheckedText = None

		sp = SpellChecker()

		#Fill in code here
		
		spellCheckedText = []
		for s in text:
			tempSentence = []
			for w in s:
				tempSentence.append(sp.correction(w))
			spellCheckedText.append(tempSentence)


		return spellCheckedText




	