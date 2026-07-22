class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            
            while num > 0:
                r = num % 10
                total = total + r
                num = num // 10
            
            num = total
        
        return num            
        