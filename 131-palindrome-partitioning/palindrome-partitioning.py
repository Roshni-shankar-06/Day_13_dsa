class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def dfs(start: int, path: list[str]) -> None:
           
