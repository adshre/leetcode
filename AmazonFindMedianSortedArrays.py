class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2) :
            return self.findMedianSortedArrays(nums2, nums1)
        
        x = len(nums1)
        y = len(nums2)
        
        low = 0
        high = x
        while low <= high :
            partitionX = (low + high) // 2
            partitionY =  (x + y + 1) //2 - partitionX

            maxLeftX = float(-inf) if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float(inf) if partitionX == x else nums1[partitionX]

            maxLeftY = float(-inf) if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float(inf) if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX :
                if (x + y) % 2 == 0 :
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY) )/ 2
                else :
                    return max(maxLeftX, maxLeftY) 
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else :
                low = partitionX + 1
        return -1
      
      
 class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        res = []
        i,j = 0, 0
        while i < nums1Len and j < nums2Len :
            if nums1[i] < nums2[j] :
                res.append(nums1[i])
                i = i + 1
            else :
                res.append(nums2[j])
                j = j + 1
        res = res + nums1[i:] + nums2[j:] 
        
        median = res[len(res)//2] if len(res)%2 !=0 else (res[len(res)//2] + res[len(res)//2 - 1])/2
        return median
                
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        i = 0
        j = 0
        
        extra = []
        
        if m == 0 :
            return median(nums2)
        if n == 0 :
            return median(nums1)
        
        while i < m and j < n :
            if nums1[i] <= nums2[j]:
                extra.append(nums1[i])
                i += 1
                
            elif nums1[i] >= nums2[j]:
                extra.append(nums2[j])
                j += 1
        print( i , j)
        if i == m and j < n :
            for k in range(j, n):
                extra.append(nums2[k])
        if i < m and j == n :
            for k in range(i, m):
                extra.append(nums1[k])
        
        print(extra)
        
        return median(extra)
                
            
        
    def median(nums: List[int]):
        X = len(nums)
        if X % 2 == 0:
            return (nums[X//2] + nums[(X-1)//2])/2
        else :
            return nums[X//2]
