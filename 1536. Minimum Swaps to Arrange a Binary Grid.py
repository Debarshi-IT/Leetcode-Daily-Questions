class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        z = []
        for r in range(n):
            c = n - 1
            cnt = 0
            while c >= 0 and grid[r][c] == 0:
                cnt += 1
                c -= 1
            z.append(cnt)
        ans = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and z[j] < need:
                j += 1
            if j == n:
                return -1 
            while j > i:
                z[j], z[j - 1] = z[j - 1], z[j]
                ans += 1
                j -= 1
        return ans
