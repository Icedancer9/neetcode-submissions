class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Create an adjacency list first and do a dfs on the adj list
        # If I did not touch all the nodes, then increment the number of
            # connected components and go to the next node that is not part of the 
            # explored component 
        
        adj = {i:[] for i in range(n)}
        for pair in edges:
            adj[pair[0]].append(pair[1]) # adj[0] = [1]
            adj[pair[1]].append(pair[0]) # adj[1] = [0]
        # {0:[1,2], 1:[0,2], 2:[0,1]}
        # For this traversal, we keep track of the nodes in our path and just 
        # iterate through all the nodes in each adj list key.
            # Even though the above graph makes a cycle, once we iterate through all the nodes
            # in each list, we can exit out of the loop
        # path = [0, 1, 2]
        # Reset the path when entering the dfs function
        path = set()
        ans = 0
        def dfs(node):
            if node in path:
                return 
            
            path.add(node)
            for child in adj[node]:
                dfs(child)
            return 
        
        for k in adj:
            if k not in path:
                ans += 1
                dfs(k)
        return ans 

