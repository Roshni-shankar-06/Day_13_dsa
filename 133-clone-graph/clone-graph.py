class Solution:
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.map:
     
      
