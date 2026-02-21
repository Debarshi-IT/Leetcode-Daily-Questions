class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p = {2, 3, 5, 7, 11, 13, 17, 19}
        tmp = [bin(i)[2:] for i in range(left, right + 1)]
        op = 0        
        for i in tmp:
            c = 0
            for j in i:
                if j == '1':
                    c += 1
            if c in p:
                op += 1                
        return op
