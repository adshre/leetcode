class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)  # initializing answer as key and list value
        for s in strs :
            ans[tuple([sorted(s)])].append(s) # sorted elements group together as tuple key and string as value
        return ans.values() # return only ans
