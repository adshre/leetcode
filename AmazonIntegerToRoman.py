class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X" , "IX", "V", "IV", "I"]
        numbers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        
        for letter, n in zip(symbols, numbers):  # use dictionary to club symbol with number
            res += letter * (num//n) # Symbol * input // num from dictionary. 
            """
            eg =>
            1994 = M * 1994 //1000 =  M * 1
            994 = CM * 994 // 900 = CM * 1
            94 = D * 94 // 500 = D * 0 .....
            
            """
            num %= n  
            """
            num = 1994 % 1000 = 994
            num = 994 % 900 = 94
            num = 94 % 500 = 94 ......
            """
            
        return res
        
        or
        
        for i, n in enumerate(numbers): # using enumerate 
            res += symbols[i] * (num//n)
            num %=n
        return res
    
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0: break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)
