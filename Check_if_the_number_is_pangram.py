class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(sentence)):
            print(sentence[i])
            try:
                alphabet.remove(sentence[i])
            except:
                pass
            if not alphabet:
                return True
        return False
