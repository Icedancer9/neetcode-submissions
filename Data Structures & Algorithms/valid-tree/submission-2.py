class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Keep track of which node you previously came from 

        d = {i:[] for i in range(n)}
        for pair in edges:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])
        
        seen = set()

        # Base case: 
            # stop if we detect a cycle 
        def dfs(node, prev_node):

            if node in seen:
                return False
            
            seen.add(node)
            for edge in d[node]:
                if edge == prev_node:
                    continue
                
                if not dfs(edge, node):
                    return False 
            return True

        return dfs(0,-1) and len(seen) == n



     