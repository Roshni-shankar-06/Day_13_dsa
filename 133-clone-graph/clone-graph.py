class Solution:
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.map:
            return self.map[node]
        
        newNode = Node(node.val, [])
        self.map[node] = newNode
    
