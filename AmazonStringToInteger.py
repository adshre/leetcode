class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:  # test case of only white spaces / no char in string
            return 0
        sign = 1  # to check positive or negative
        num = ""
        if s[0] == '-':
            sign = -1
            s = s[1:]  # to remove special character check of is digit, other cahr like '.' included in check
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        for each in s:
            if not each.isdigit(): #check if not digit
                break  # get out of loop
            num = num + each  # add to answe
        if len(num) == 0 :  # if nothing is added in ans, all alpha char or special char
            return 0
        else :
            num = int(num)  # convert string to int
            if sign == -1 :
                num = -1 * num  # to negative 
                return max(-2 ** 31, num)  # To return in range if negative 
            return min(2 ** 31 -1 , num)  # To return in range if positive
            
OR
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)
        
