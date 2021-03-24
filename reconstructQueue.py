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
        
"""
https://leetcode.com/problems/queue-reconstruction-by-height/

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

"""
