class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(
            map(len,s.replace('01','0 1').replace('10','1 0').split()))))
