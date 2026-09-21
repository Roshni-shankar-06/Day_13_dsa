class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def dfs(start: int, path: list[str]) -> None:
            if start == len(s):
                ans.append(path.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    dfs(end, path)
                    path.pop()  # Backtrack
                    
        dfs(0, [])
        return ans
