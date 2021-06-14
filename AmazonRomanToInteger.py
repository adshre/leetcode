class Solution:
    def romanToInt(self, s: str) -> int:
     
        mp = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        ans = mp.get(s[-1])
        for i in reversed(range(len(s)-1)):
            if mp[s[i]]< mp[s[i+1]]:
                ans -= mp[s[i]]
            else :
                ans += mp[s[i]]
        return ans
        
        
 class Solution:
    def romanToInt(self, s: str) -> int:
     
        mp = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        lst = []
        for i in reversed(range(len(s))):
            if s[i] in mp :
                lst.append(mp[s[i]])
        #print(lst)
        ans = lst[0]
        for i in range(1,len(lst)):
            if lst[i] < lst[i-1]:
                ans -= lst[i]
            else:
                ans += lst[i]
        return ans
