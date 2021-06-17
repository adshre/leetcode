class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # for two pointers sorted array needed
        diff = float('inf')  # intialize diff to max value
        for i in range(len(nums)-2):  # run loop till len(nums) or till len(nums)-2
            lo = i + 1 
            hi = len(nums) - 1
            while lo < hi :
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):  # checking if abs of target- sum is less than diff
                    diff = target - sum # assign to diff
                elif sum < target:
                    lo += 1
                else :
                    hi -= 1
            if diff == 0:  # if diff is zero break
                break
        return target - diff  # as sum = target - diff
      
      
      
 """
 Remaining : Binary Search Approach
 
 
Above code Algorithm :

Initialize the minimum difference diff with a large value.
Sort the input array nums.
Iterate through the array:
  For the current position i, set lo to i + 1, and hi to the last index.
  While the lo pointer is smaller than hi:
      Set sum to nums[i] + nums[lo] + nums[hi].
      If the absolute difference between sum and target is smaller than the absolute value of diff:
        Set diff to target - sum.
      If sum is less than target, increment lo.
      Else, decrement hi.
  If diff is zero, break from the loop.
Return the value of the closest triplet, which is target - diff.
 """
