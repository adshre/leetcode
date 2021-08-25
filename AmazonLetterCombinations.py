class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            if len(path) == len(digits):      # if permutation len and number of digit length matches then we have the last complete solution so we return
                combinations.append("".join(path))
                return
            
            possible_letters = mp[digits[index]]     # find all possible letters combo in the digit from the map ex : index = 0, digits[0] = 3 in case of 23 and mp [3] would be def
            for each in possible_letters: # since string directly take for each
                path.append(each)   # add each letter to path
                backtrack(index + 1, path)   # backtrack to next digit , eg : 2 in case of 23 and follow the same
                path.pop()    #pop last added 
            
        combinations = []
        backtrack(0,[])
        return combinations
        
        
