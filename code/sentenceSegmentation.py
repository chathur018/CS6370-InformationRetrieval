from util import *

# Add your import statements here




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here

		segmentedText = []
		sentenceEndChars = [".", "?", "!"]
		whiteSpaceChars = [" ", "\n", "\t"]
		prev = 0
		curr = 0
		sentenceBegin = False
		for a in text:
			curr += 1
			if not sentenceBegin:
				for c in whiteSpaceChars:
					if c == a:
						prev += 1
						break
					else:
						sentenceBegin = True
			for b in sentenceEndChars:
				if a == b:
					segmentedText.append(text[prev:curr])
					prev = curr
					sentenceBegin = False
		
		if not prev == curr:
			segmentedText.append(text[prev:curr])

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		#Fill in code here

		segmentedText = nltk.sent_tokenize(text)
		
		return segmentedText