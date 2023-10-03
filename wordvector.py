import math

class WordVector:
    """класс для создания матрицы tf, idf, tf-idf, ngrams по умолчанию 1"""
    def __init__(self, getlist, tfidf = "tf-idf", ngrams = 1):
        self.getlist = getlist
        self.tfidf = tfidf
        self.ngrams = ngrams

    def indexing(self, arg):
        """индексация"""
        self.arg = arg
        self.ind = 0
        memo = {}
        for i in self.arg:
            if i not in memo.keys():
                triallist = []
                triallist.append((self.ind, 1))
                memo[i] = triallist
            else:
                triallist = []
                w = memo[i]
                triallist.append((self.ind, w[0][1] + 1))
                memo[i] = triallist
        return memo

    def fngrams(self, text, ngram):
        self.text = text
        self.ngram = ngram
        nlist = []
        for i in self.text:
            trlist = []
            for x, j in enumerate(i):
                tc = ""
                tx = x
                for k in range(self.ngram):
                    if k == 0:
                        tc = str(i[tx])
                    elif k > 0:
                        try:
                            tc += " " + str(i[tx])
                        except IndexError:
                            break
                    trlist.append(tc)
                    tx += 1
            nlist.append(trlist)
        return nlist

    def load(self):
        """вектор"""
        klist = []
        instv = []
        countw = 0
    
        if self.ngrams >= 1 and self.ngrams <= 4:
            glist = self.fngrams(self.getlist, self.ngrams)
            for i in glist:
                for j in i:
                    instv.append(j)

        elif self.ngrams == 1:
            for i in self.getlist:
                for j in i:
                    instv.append(j)
            glist = self.getlist.copy()

        if self.tfidf == "tf" and len(self.getlist) != 1:
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                ind = self.indexing(i)
                for j in i:
                    countw += 1
                    c = ind[j]
                    tlist.append([c[0][1] / len(instv)])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return instv, klist

        elif self.tfidf == "idf" and len(self.getlist) != 1:
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                for j in i:
                    countw += 1
                    tlist.append([math.log10(len(glist)/sum([1.0 for i in glist if j in i]))])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return instv, klist

        elif self.tfidf == "tf-idf" and len(self.getlist) != 1:
            for i in glist:
                tlist = []
                tlist2 = []
                if countw != 0:
                    tlist.append([0] * countw)
                ind = self.indexing(i)
                for j in i:
                    countw += 1
                    c = ind[j]
                    vartf = c[0][1] / len(instv)
                    varidf = math.log10(len(glist)/sum([1.0 for i in glist if j in i]))
                    tlist.append([vartf * varidf])
                tlist.append([0] * (len(instv) - countw))
                for k in tlist:
                    tlist2.extend(k)
                klist.append(tlist2)
            return instv, klist
        else:
            for i in glist:
                tlist = []
                for j in i:
                    tlist.append(1)
                klist.append(tlist)
            return instv, klist
