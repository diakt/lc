// 1. Two Sum
// https://leetcode.com/problems/two-sum/

//pretty quick find
// rt 92, mem 36


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    length = nums.length
    dingo = {}
    for(i=0;i<length;i++){
        if (nums[i] in dingo){
            return [dingo[nums[i]], i]
                    }
        dingo[(target-nums[i])] = i
        
    }
};