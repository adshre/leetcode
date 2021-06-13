class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        ans = 0
        
        for j in range(len(s)) :
            if s[j] in mp : # if elem in map
                i = max(i, mp[s[j]]) # move index of start(i) to new position
            ans = max(ans, j-i+1) # ans is max of ans and sliding window
            mp[s[j]] = j + 1 # map element to curr index + 1 , 
        return ans
     """
     Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
     If s[j] in duplicate range(i,j), we don't need to increment i little by little we can skip all elements  in range[i,j] and let i be j+1 directly
     """
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0
        N = len(s)
        mp = {}
        ans = 0
        
        while(j < N) :
            if s[j] in mp:
                mp[s[j]] += 1
            else :
                mp[s[j]] = 1
                
            if len(mp) > j - i + 1:
                j = j + 1
            elif len(mp) == j - i + 1:
                ans = max(ans , j - i + 1)
                j = j + 1
            elif len(mp) < j - i + 1 :
                while (len(mp) < j - i + 1) :
                    mp[s[i]] -= 1
                    if mp[s[i]] == 0 :
                        mp.pop(s[i])
                    i = i + 1
                j = j + 1
        return ans
                
