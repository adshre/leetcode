class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        V1 = version1.split('.')
        V2 = version2.split('.')
        
        n1, n2 = len(V1), len(V2)
        
        for i in range(max(n1, n2)):
            """
               Taking ith digits and comparing if same move to next digit else whenever first greatest digit occurs , get 1 or -1 accordingly.
            """
            x = int(V1[i]) if i < n1 else 0   
            y = int(V2[i]) if i < n2 else 0
            
            if x != y:
                return 1 if x > y else -1
        
        return 0
