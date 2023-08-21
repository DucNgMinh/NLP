import pandas as pd

class Minimum_edit_distance():
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def normal_distance(self):
        m = len(self.word1)
        n = len(self.word2)
        df = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            df[i][0] = i

        for j in range(n + 1):
            df[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    df[i][j] = df[i - 1][j - 1]
                else:
                    df[i][j] = min(df[i - 1][j] + 1, 
                                   df[i][j - 1] + 1, 
                                   df[i - 1][j - 1] + 1)

        return df[m][n]

    def levenshtein_distance(self):
        m = len(self.word1)
        n = len(self.word2)
        df = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            df[i][0] = i

        for j in range(n + 1):
            df[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    df[i][j] = df[i - 1][j - 1]
                else:
                    df[i][j] = min(df[i - 1][j] + 1, 
                                   df[i][j - 1] + 1, 
                                   df[i - 1][j - 1] + 2)

        return df[m][n]

w1 = 'intention'
w2 = ''
tst = Minimum_edit_distance(w1, w2)
print(tst.normal_distance())
print(tst.levenshtein_distance())