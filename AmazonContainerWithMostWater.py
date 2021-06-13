class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Area = length of shorter vertical line * distance between lines
        l = 0   # first pointer to left
        r = len(height) - 1  # second pointer to last
        max_area = 0 
        
        while(l < r): 
            w = r - l  # finding width
            lv = height[l]  # initialize left vertical 
            lr = height[r]  # initialize right vertical
            if lv < lr :  
                h = lv      # since left is short make it new height 
                l = l + 1   # increment to next
            else :
                h = lr     # since right is short make it new height 
                r = r - 1  # decrement to previous
            max_area = max(max_area, h * w)  # keep track of max_area 
        return max_area
        
        
