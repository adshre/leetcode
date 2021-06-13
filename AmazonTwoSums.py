class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {} #create map to store nums
        
        for i in range(len(nums)) :  #loop through array
            complement  = target - nums[i] #target = sum + target - sum so take complement
            
            """
              check if complement present in map , no need of stored[complement] != i ,
              i.e checking if complement is at same index : eg = [3,3] as we are doing one pass hashmap and storing data later in map.
            """
            if complement in stored : 
                return [i, stored[complement]]. # if complement found return answer
            else :
                stored[nums[i]] = i # else add number  to map stored
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapDict = {}
    
        for i, n in enumerate(nums):  # Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. eg: (0, "egg") in [egg]
            complement = target - n
            if complement in mapDict.keys():
                return[i, mapDict[complement]]
            mapDict[n] = i
            
            
            
            
            
