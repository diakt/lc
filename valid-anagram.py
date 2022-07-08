# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# quad for loop w/dictionary
# 16 rt, 53 mem
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create dictionary with first argument letters
        dingo = dict((str(letter), 0) for letter in s)
        #iterate through for loop to determine frequency
        for letter in s:
            dingo[str(letter)] +=1
        #now have dictionary with kvp for letter and frequency
        for secondLetter in t:
            if dingo.has_key(secondLetter) == False:
                return False
            dingo[str(secondLetter)] -= 1
        #now SHOULD have (if anagram) a dictionary of 0s
        print(dingo)
        for finalVal in dingo.values():
            print(finalVal)
            if finalVal != 0:
                return False

        return True
    
#oof, removed dict def
#8 rt, 89 mem

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create dictionary with first argument letters
        dingo = dict()
        #iterate through for loop to determine frequency
        for letter in s:
            if str(letter) in dingo:
                dingo[str(letter)] +=1
            else:
                dingo[str(letter)] = 1
        #now have dictionary with kvp for letter and frequency
        for secondLetter in t:
            if dingo.has_key(secondLetter) == False:
                return False
            dingo[str(secondLetter)] -= 1
        #now SHOULD have (if anagram) a dictionary of 0s
        print(dingo)
        for finalVal in dingo.values():
            print(finalVal)
            if finalVal != 0:
                return False

        return True
    

# asdfasdfasdf
#8 rt, 64 mem

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create dictionary with first argument letters
        dingo = dict((str(letter), 0) for letter in s)
        #iterate through for loop to determine frequency
        for letter in s:
            dingo[str(letter)] +=1
        #now have dictionary with kvp for letter and frequency
        for secondLetter in t:
            if dingo.has_key(str(secondLetter)) == False:
                return False
            else:
                dingo[str(secondLetter)] -= 1
        #now SHOULD have (if anagram) a dictionary of 0s
        print(dingo)
        for finalVal in dingo.values():
            print(finalVal)
            if finalVal != 0:
                return False

        return True

    

# focused on not casting unic to str
# 78 rt, 50 mem

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create dictionary with first argument letters
        dingo = dict((letter, 0) for letter in s)
        #iterate through for loop to determine frequency
        for letter in s:
            dingo[letter] +=1

        #now have dictionary with kvp for letter and frequency
        for secondLetter in t:
            if dingo.has_key(secondLetter) == False:
                return False
            dingo[secondLetter] -= 1



        #now SHOULD have (if anagram) a dictionary of 0s
        print(dingo)
        for finalVal in dingo.values():
            print(finalVal)
            if finalVal != 0:
                return False

        return True



# neetcode recommended version

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True






#my version
# 49 rt, 26 mem

class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)):
            return False
        
        sHash, tHash = {}, {}

        for i in range(len(s)):
            sHash[s[i]] = 1 + sHash.get(s[i], 0)
            tHash[t[i]] = 1 + tHash.get(t[i], 0)
            # this is huge that get can supply alternate value
        for value in sHash:
            if sHash[value] != tHash.get(value,0): 
                #note if we have val in sHash, it won't be 0
                return False
        return True

        