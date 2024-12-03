class Solution(object):
    def closeStrings(self, word1, word2):
        wordhas1={}
        wordhas2={}
        for i in word1:
            if i in wordhas1:
                wordhas1[i]+=1
            else:
                wordhas1[i]=1
        for i in word2:
            if i in wordhas2:
                wordhas2[i]+=1
            else:
                wordhas2[i]=1
        if (sorted(wordhas1.keys())==sorted(wordhas2.keys())) and (sorted(wordhas1.values())==sorted(wordhas2.values())):
            return True
        return False
