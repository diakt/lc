# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# brute force
# 17% rt, 68% mem
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        output = None
        i=0
        j=0

        for numbers in nums: 
            firstpoint = nums[i]
            j = i+1
            
            for secondnumbers in range(i+1, len(nums)):
                secondpoint = nums[j]
                if firstpoint+secondpoint == target:
                    output = [i, j]
                    return output
                j+=1
            
            i+=1

# dictionary 1
# 79% rt, 44% mem
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        numberDict = {}
        for idx, val in enumerate(nums):
            difference = target - val
            if difference in numberDict:
                return [numberDict[difference], idx]
            numberDict[val] = idx

#dictionary 2, someone else
#72% rt, 68% mem
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        numberDict = {}
        for idx, val in enumerate(nums):
            if val in numberDict:
                return [numberDict[val], idx]
            numberDict[target-val] = idx
        
                