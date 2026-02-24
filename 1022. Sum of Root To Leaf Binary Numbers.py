class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path = []
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                s = ''.join(str(v) for v in path)
                ans += int(s, 2)
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()
        dfs(root)
        return ans
