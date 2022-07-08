# 12341234. Valid Parentheses
# 23 rt, 32 mem
#not great
# but figured it out decently quickly, could use hashtable

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for char in s:
            if char in {'(', '[', '{'}:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if validator(stack.pop(), char):
                    pass
                else:
                    return False
                    
        if len(stack) == 0:
            return True
            
def validator(char1, char2):
    if char1 == '(' and char2 == ')':
        return True
    elif char1 == '{' and char2 == '}':
        return True
    elif char1 == '[' and char2 == ']':
        return True
    else:
        return False

#better solution
# 48 rt, 69 mem

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openClose = {"}":"{", "]":"[", ")":"("}
        stack = []
        for x in s:
            if x in openClose:
                if not stack:
                    return False
                if openClose[x] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(x)
                
        if len(stack) == 0:
            return True



#faster solution
# 83 rt, 32 mem

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openClose = {"}":"{", "]":"[", ")":"("}
        stack = []
        for x in s:
            if x in openClose:
                if stack and openClose[x] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(x)
                
        if len(stack) == 0:
            return True

#neetcode printed code
#37 rt, 12 mem

class Solution:
    def isValid(self, s):
        openClose = { ")":"(", "]":"[", "}":"{"}
        stack = []
        
        # conditions
        for c in s:
            if c not in openClose:
                stack.append(c)
                continue
            if (not stack) or stack[-1] != openClose[c]:
                return False

            stack.pop()
        
        
        return not stack

#my take on neetcode video take
# 52 rt 81 mem

class Solution:
    def isValid(self, s):
        openClose = { ")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in openClose:
                if stack and stack[-1] == openClose(c):
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        return False if stack else True


#neetcode video take
# 89 rt, 59 mem

class Solution:
    def isValid(self, s):
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack

