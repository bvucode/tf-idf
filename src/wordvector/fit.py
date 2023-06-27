
class Fit:
    """класс поиска в матрице """
    def __init__(self, bow1, vect, bow2, vect2):
        self.bow1 = bow1
        self.bow2 = bow2
        self.vect = vect
        self.vect2 = vect2

    def fit(self):
        """находит максимальное количество совпадений в векторах"""
        memo = []
        mdict = {}
        searchlist = []
        for i, x in enumerate(self.bow1):
            for k, y in enumerate(self.bow2):
                if y == x:
                    for j in range(len(self.vect)):
                        if self.vect[j][i] != 0:
                            mdict[x] = self.vect[j][i]
                    searchlist.append((y, k))

        if len(searchlist) != 0:
            for i in range(len(self.vect2)):
                triallist = []
                triallist2 = []
                for j in searchlist:
                    if self.vect2[i][j[1]] != 0:
                        triallist2.append(self.vect2[i][j[1]])
                        if j[0] in mdict.keys():
                            triallist.append(mdict[j[0]])
                memo.append((i, triallist, triallist2))
        return memo
