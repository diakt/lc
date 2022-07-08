# 217. Contains Duplicate
# https://leetcode.com/problems/two-sum/

# first shot through neetcode
# 72% rt, 42% mem
# used hashmap, enumerate as well
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for idx, i in enumerate(nums):
            if i in hashmap:
                print(str(i) + "is in nums")
                return True
            hashmap[i] = idx
            
        return False

# neetcode recommended approach:
def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
#uses hashset, which is like a dictionary but just one value, so that's a good thing to pickup
# also the List[whatever] exists to define the input and output
#so expects a list of int values, wants a bool
# cool stuff