from util import *

# Add your import statements here




class LSA():

	def __init__(self):
		self.index = None
		self.idf = None
		self.idfzero = None
		self.scores = None
		self.k = None
		self.updatedIndex = None

	def buildIndex(self, docs, docIDs, k):

		self.k = k
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
			for sent in doc:
				for word in sent:
					if word in tempIndex:
						tempIndex[word] += 1
					else:
						tempIndex[word] = float(1)
			for i in tempIndex:
				index[i][id] = tempIndex[i]# * idf[i]

		self.index = index
		self.idf = idf

		typeMap = {}
		i = 0
		termDoc = np.zeros((len(index), len(docIDs)))

		for term in index:
			typeMap[term] = i
			for doc in index[term]:
				termDoc[i][doc-1] = index[term][doc]
			i += 1

		U, S, Vh = np.linalg.svd(termDoc)
		U = U[:, :k]
		S = np.diag(S[:k])
		Vh = Vh[:k]

		updatedTDM = U @ S @ Vh
		updatedIndex = {}
		for type in typeMap:
			updatedIndex[type] = {}

		for id in docIDs:
			tempIndex = {}
			magnitude = float(0)
			for type in typeMap:
				tempIndex[type] = updatedTDM[typeMap[type]][id-1] * self.idf[type]
				magnitude += tempIndex[type] ** 2
			magnitude = math.sqrt(magnitude)
			for type in typeMap:
				updatedIndex[type][id] = tempIndex[type] / magnitude
		
		self.updatedIndex = updatedIndex


	def rank(self, queries):
		doc_IDs_ordered = []
		self.scores = []

		for query in queries:
			tempIndex = {}
			magnitude = float(0)
			scores = {}
			for sent in query:
				for word in sent:
					if word in self.updatedIndex:
						for i in self.updatedIndex[word]:
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
				if i in self.updatedIndex:
					for j in self.updatedIndex[i]:
						scores[j] += tempIndex[i] * self.updatedIndex[i][j]
			self.scores.append(scores)
			scores = sorted(scores.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
			ranks = []
			for s in scores:
				ranks.append(s[0])
			doc_IDs_ordered.append(ranks)
	
		return doc_IDs_ordered
