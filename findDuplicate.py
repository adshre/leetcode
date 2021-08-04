class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        
        while low <= high :
            currMid = (low + high) // 2
            count = 0
            count = sum(num <= currMid for num in nums)
            if count > currMid :
                duplicate = currMid
                high = currMid - 1
            else :
                low = currMid + 1
        return duplicate
        
        
##################
https://leetcode.com/problems/find-the-duplicate-number/solution/

