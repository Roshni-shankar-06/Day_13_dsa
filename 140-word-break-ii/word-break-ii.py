class Solution:
  def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) -> list[str]:
      ans = []

      # 1 <= len(prefix) < len(s)
      for i in range(1, len(s)):
        prefix = s[:i]
        suffix = s[i:]
    
