class Solution:
    def longestBalanced(self, l: List[int]) -> int:
        n = len(l)
        m = 1 << n.bit_length()
        mx = [0] * (m << 1)
        mn = [0] * (m << 1)
        lz = [0] * (m << 1)
        last = {}
        ans = cur = 0
        def ctz(i): return (i & -i).bit_length() - 1

        def update(i, v):
            mx[i] += v
            mn[i] += v
            lz[i] += v
        def push(i):
            h = i.bit_length()
            i |= m
            while h:
                j = i >> h
                if t := lz[j]:
                    update(j << 1, t)
                    update(j << 1 | 1, t)
                    lz[j] = 0
                h -= 1
        def pull(i):
            i |= m
            while i > 1:
                i >>= 1
                mx[i] = max(mx[i << 1], mx[i << 1 | 1]) + lz[i]
                mn[i] = min(mn[i << 1], mn[i << 1 | 1]) + lz[i]
        def add(i, v):
            push(i)
            s, t = i | m, m << 1
            while s < t:
                z = ctz(s)
                s >>= z
                t >>= z
                if s == t: break
                update(s, v)
                s += 1
            pull(i)
        def query(v):
            i = 1
            while i < m:
                if t := lz[i]:
                    update(i << 1, t)
                    update(i << 1 | 1, t)
                    lz[i] = 0
                i <<= 1
                if not mn[i] <= v <= mx[i]:
                    i |= 1
            return i - m
        for i, v in enumerate(l, 1):
            x = 1 if v & 1 else -1
            if pi := last.get(v):
                cur -= x
                add(pi, -x)
            cur += x
            add(i, x)
            last[v] = i
            ans = max(ans, i - query(cur))
        return ans
