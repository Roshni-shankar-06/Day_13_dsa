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
              
