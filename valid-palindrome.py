# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

# Fairly reasonable, remembered the a[::-1] thing which was awesome. Need to learn regex
# 65 rt, 19 mem

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = lower(re.sub(r'[^a-zA-Z0-9]', '', s))
        b = a[::-1]
        if a ==b:
            return True
        return False

#so looking at neetcode, this is a two pointer problem
# another thing I could do also is use isalphanum to for loop characters of a string and add if suitable
#need to implement the neetcode but tomorrow I guess


