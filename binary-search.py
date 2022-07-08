# 704. Binary Search
# https://leetcode.com/problems/binary-search/

#pure testicular fortitude
#pointers do not do well
#avoid variabling in while loops for little things
#if you are guiding based off of index vs values in a while, check your shit out head to toe
#base case low, check edge cases early, then find long string, don't do middle
# rt 83, mem 52

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        if l == r :
            if nums[l] == target:
                return l
            else:
                return -1

        while l < r:
            print(l, r)
            print("left val is " + str(nums[l]))
            print("right val is " + str(nums[r]))
            if nums[l+(r-l)/2] == target: #marry
                return l+(r-l)/2
            elif r-l == 1:
                if nums[r] == target:
                    return r
                elif nums[l] == target:
                    return l
                else:
                    return -1
            elif nums[l+(r-l)/2] < target:
                l = l+(r-l)/2

            elif nums[l+(r-l)/2] > target:
                r = r-(r-l)/2
            