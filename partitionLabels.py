class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        #creating dictionary having max index of character's last occurence 
        # {'a' : 8, 'b' : 5 ,.....}
        last_occurence = {c : i for i, c in enumerate(S)}
        
        #initializing partition start and end, also declaring ans.
        start_of_partition = end_of_partition = 0
        answer = []
        
        #going through each character in input string
        for i,c in enumerate(S):
            # intialising that end partition is max of current character index                  and last occurence value.
            # max(0, 8)
            end_of_partition = max(end_of_partition, last_occurence[c])
            # if index and end of partition are same 
            # 8 == 8
            if i == end_of_partition:
                # answer is range + 1 
                # (8 - 0 + 1) => 9
                answer.append(i - start_of_partition + 1)
                # moving to next partition
                # 8 + 1 => 9
                start_of_partition = i+1
        return answer
    

    """
    https://leetcode.com/problems/partition-labels/
    
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    """
