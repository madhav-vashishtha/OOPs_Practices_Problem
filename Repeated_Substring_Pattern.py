class RepeatedSubstringChecker:
    def __init__(self, s):
        self.s = s

    def repeated_substring_pattern(self):
        n = len(self.s)


        for l in range(1, n // 2 + 1):
            if n % l == 0:
                sub = self.s[:l]
                if sub * (n // l) == self.s:
                    return True
                

        return False
    
obj = RepeatedSubstringChecker("abab")
print(obj.repeated_substring_pattern())   

obj = RepeatedSubstringChecker("aba")
print(obj.repeated_substring_pattern())  

obj = RepeatedSubstringChecker("abcabcabcabc")
print(obj.repeated_substring_pattern())   
