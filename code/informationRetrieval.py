from util import *

# Add your import statements here




class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.idf = None
		self.idfzero = None
		self.scores = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None

		#Fill in code here

		index = {}
		idf = {}

		for (doc, id) in zip(docs, docIDs):
			words = []
			for sent in doc:
				for word in sent:
					if word not in words:
						words.append(word)
			for word in words:
				if word not in idf:
					idf[word] = float(0)
					index[word] = {}
				idf[word] += 1
		
		self.idfzero = math.log2(len(docIDs)+len(idf))
		for w in idf:
			idf[w] = math.log2((len(docIDs)+len(idf)) / (idf[w]+1))

		for (doc, id) in zip(docs, docIDs):
			tempIndex = {}
			magnitude = float(0)
			for sent in doc:
				for word in sent:
					if word in tempIndex:
						tempIndex[word] += 1
					else:
						tempIndex[word] = float(1)
			for i in tempIndex:
				tempIndex[i] *= idf[i]
				magnitude += tempIndex[i] ** 2
			magnitude = math.sqrt(magnitude)
			for i in tempIndex:
				index[i][id] = tempIndex[i] / magnitude

		self.index = index
		self.idf = idf


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []
		self.scores = []

		#Fill in code here

		for query in queries:
			tempIndex = {}
			magnitude = float(0)
			scores = {}
			for sent in query:
				for word in sent:
					if word in self.index:
						for i in self.index[word]:
							if i not in scores:
								scores[i] = float(0)
					if word not in tempIndex:
						tempIndex[word] = float(0)
					tempIndex[word] += 1
			for i in tempIndex:
				if i in self.idf:
					tempIndex[i] *= self.idf[i]
				else:
					tempIndex[i] *= self.idfzero
				magnitude += tempIndex[i] ** 2
			magnitude = math.sqrt(magnitude)
			for i in tempIndex:
				tempIndex[i] = tempIndex[i] / magnitude
			for i in tempIndex:
				if i in self.index:
					for j in self.index[i]:
						scores[j] += tempIndex[i] * self.index[i][j]
			self.scores.append(scores)
			scores = sorted(scores.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
			ranks = []
			for s in scores:
				ranks.append(s[0])
			doc_IDs_ordered.append(ranks)
	
		return doc_IDs_ordered




