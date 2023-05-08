from util import *
from informationRetrieval import InformationRetrieval

class Bigram():

    def __init_(self):
        self.index = None
        self.idf = None
        self.idfzero = None
        self.unigram = None
        self.docsIDs = None
    
    def buildIndex(self, docs, docIDS):
        index = {}
        idf = {}
        self.docsIDs = docIDS

        for (doc, id) in zip(docs, docIDS):
            bigrams = []
            for sent in doc:
                for i in range(len(sent)-1):
                    if (sent[i], sent[i+1]) not in bigrams:
                        bigrams.append((sent[i], sent[i+1]))
            for b in bigrams:
                if b not in idf:
                    idf[b] = float(0)
                    index[b] = {}
                idf[b] += 1
        
        #print(idf[('boundary', 'layer')])
        
        self.idfzero = math.log2(len(docIDS)+len(idf))
        for b in idf:
            idf[b] = math.log2((len(docIDS)+len(idf)) / (idf[b]+1))
        
        for (doc, id) in zip(docs, docIDS):
            tempIndex = {}
            magnitude = float(0)
            for sent in doc:
                for i in range(len(sent)-1):
                    b = (sent[i], sent[i+1])
                    if b in tempIndex:
                        tempIndex[b] += 1
                    else:
                        tempIndex[b] = float(1)
            for i in tempIndex:
                tempIndex[i] *= idf[i]
                magnitude += tempIndex[i]**2
            magnitude = math.sqrt(magnitude)
            for i in tempIndex:
                index[i][id] = tempIndex[i] / magnitude
        
        self.index = index
        self.idf = idf
        self.unigram = InformationRetrieval()
        self.unigram.buildIndex(docs, docIDS)
        print(len(self.unigram.index))

    def hybridrank(self, queries):
        doc_IDs_ordered = []

        self.unigram.rank(queries)
        uscores = self.unigram.scores

        num = 0
        for query in queries:
            tempIndex = {}
            magnitude = float(0)
            scores = {}
            for sent in query:
                for i in range(len(sent)-1):
                    b = (sent[i], sent[i+1]) 
                    if b in self.index:
                        for j in self.index[b]:
                            if j not in scores:
                                scores[j] = float(0)
                    if b not in tempIndex:
                        tempIndex[b]  = float(0)
                    tempIndex[b] += 1
            for i in tempIndex:
                if i in self.idf:
                    tempIndex[i] *= self.idf[i]
                else:
                    tempIndex[i] *= self.idfzero
                magnitude += tempIndex[i] ** 2
            magnitude = math.sqrt(magnitude)
            for i in tempIndex:
                tempIndex[i] = tempIndex[i]/magnitude
            for i in tempIndex:
                if i in self.index:
                    for j in self.index[i]:
                        scores[j] += tempIndex[i] * self.index[i][j]
            for i in self.docsIDs:
                if i in scores:
                    uscores[num][i] += scores[i]
            #    else:
            #        uscores[num][i] = 0
            uscores[num] = sorted(uscores[num].items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
            ranks = []
            for s in uscores[num]:
                ranks.append(s[0])
            doc_IDs_ordered.append(ranks)
            num += 1

        return doc_IDs_ordered