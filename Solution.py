class Solution:
    def intToRoman(self, num: int) -> str:
        R = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        A = [1000, 900, 500, 400, 100, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        r = ''
        while num > 0:
            if num - A[i] >= 0:
                r = r + R[A[i]]
                num = num - A[i]
            else:
                i = i + 1
        return r
