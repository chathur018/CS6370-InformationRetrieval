from util import *

# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here

		num = 0
		i = 0
		while i < k and i < len(query_doc_IDs_ordered):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				num += 1
			i += 1
		
		precision = num / k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		
		total = 0
		next = 0
		for i in range(len(query_ids)):
			relevant = set()
			while next < len(qrels) and int(qrels[next]['query_num']) == query_ids[i]:
				relevant.add(int(qrels[next]['id']))
				next += 1
			total += self.queryPrecision(doc_IDs_ordered[i], query_ids[i], relevant, k)
		meanPrecision = total / len(query_ids)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here

		num = 0
		i = 0
		while i < k and i < len(query_doc_IDs_ordered):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				num += 1
			i += 1
		recall = num / len(true_doc_IDs)

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here

		total = 0
		next = 0

		for i in range(len(query_ids)):
			relevant = set()
			while next < len(qrels) and int(qrels[next]['query_num']) == query_ids[i]:
				relevant.add(int(qrels[next]['id']))
				next += 1
			total += self.queryRecall(doc_IDs_ordered[i], query_ids[i], relevant, k)
		meanRecall  = total / len(query_ids)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here

		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

		if precision+recall == 0:
			fscore = 0
		else:
			fscore = 2 * precision * recall
			fscore /= precision + recall

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here

		total = 0
		next = 0

		for i in range(len(query_ids)):
			relevant = set()
			while next < len(qrels) and int(qrels[next]['query_num']) == query_ids[i]:
				relevant.add(int(qrels[next]['id']))
				next += 1
			total += self.queryFscore(doc_IDs_ordered[i], query_ids[i], relevant, k)
		meanFscore  = total / len(query_ids)

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here

		relevant  = {}
		ranks = []
		for i in true_doc_IDs:
			relevant[int(i['id'])] = int(i['position'])
			ranks.append(int(i['position']))
		
		ranks.sort()

		dcgk = 0
		i = 0
		while i < k:
			if query_doc_IDs_ordered[i] in relevant:
				dcgk += (5 - relevant[query_doc_IDs_ordered[i]]) / math.log2(i+2)
			i += 1

		idcgk = 0
		i = 0
		while i < k and i < len(ranks):
			idcgk += (5 - ranks[i]) / math.log2(i+2)
			i += 1

		nDCG = dcgk / idcgk

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here

		total = 0
		prev = 0
		next = 0

		for i in range(len(query_ids)):
			while next < len(qrels) and int(qrels[next]['query_num']) == query_ids[i]:
				next += 1
			total += self.queryNDCG(doc_IDs_ordered[i], query_ids[i], qrels[prev:next], k)
			prev = next
		meanNDCG  = total / len(query_ids)

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here

		avgPrecision = 0
		i = 0
		p = 0
		while i < len(query_doc_IDs_ordered) and i < k:
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				temp = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i+1)
				avgPrecision += temp
				p += 1
			i += 1
		
		if p:
			avgPrecision /= p

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here

		total = 0
		next = 0

		for i in range(len(query_ids)):
			relevant = set()
			while next < len(q_rels) and int(q_rels[next]['query_num']) == query_ids[i]:
				relevant.add(int(q_rels[next]['id']))
				next += 1
			total += self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i], relevant, k)
		meanAveragePrecision  = total / len(query_ids)

		return meanAveragePrecision

