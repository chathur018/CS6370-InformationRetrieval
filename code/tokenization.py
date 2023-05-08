from util import *

# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here

		tokenizedText = []
		whiteSpaceChars = [" ", "\n", "\t"]
		for t in text:
			tempList = []
			prev = 0
			curr = 0
			wordBegin = False
			for a in t:
				curr += 1
				if not wordBegin:
					for c in whiteSpaceChars:
						if a == c:
							prev += 1
							break
						else:
							wordBegin = True
				else:
					for b in whiteSpaceChars:
						if a == b:
							tempList.append(t[prev:curr-1])
							prev = curr
							wordBegin = False
			
			if not prev == curr:
				tempList.append(t[prev:curr])
			tokenizedText.append(tempList)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here

		tokenizedText = []
		for t in text:
			tokenizedText.append(nltk.word_tokenize(t))

		return tokenizedText