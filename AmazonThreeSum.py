class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:   
                break
            elif i == 0 or nums[i] != nums[i-1]:
                self.twoSumsII(nums, i , res)
        return res
    
    def twoSumsII(self, nums: List[int], i: int, res: List[List[int]]):
        lo = i + 1
        hi = len(nums) - 1
        
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 :
                lo += 1
            elif sum > 0:
                hi -= 1
            else :
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                    
                    
"""
Algorithm => 
For the main function:

  Sort the input array nums.
  Iterate through the array:
    If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
    If the current value is the same as the one before, skip it.
    Otherwise, call twoSumII for the current position i.


For twoSumII function:

  Set the low pointer lo to i + 1, and high pointer hi to the last index.
  While low pointer is smaller than high:
    If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
    If sum is greater than zero, decrement hi.
    Otherwise, we found a triplet:
      Add it to the result res.
      Decrement hi and increment lo.
      Increment lo while the next value is the same as before to avoid duplicates in the result.
Return the result res.
"""
