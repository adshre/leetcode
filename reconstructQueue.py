class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        """
        sort input people list first in descending order of height(therefore -ve)
        and then if same then sort by ascending order of index value.
        
        then insert in answer list at k index the list of individual people
        """
    
        for h, k in sorted(people , key=lambda x : (-x[0],x[1])) : 
            ans.insert(k , [h, k])
        return ans
        
