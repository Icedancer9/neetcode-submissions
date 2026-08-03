class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree: an undirected graph with no cycles.
        # We need cycle detection for this algorithm

        # Cycle in a tree: encountering a vertex more than once when 
        # going down a particular path 

        """
        Invalid graph
        {0: [1,2,3],
        1: [0,2,4],
        2: [0,1],
        3: [0],
        4: [1]
    path = [0, 1, 2, ]
    prev_node = 0,1
    # prev_node to keep track of the node we just came from


        valid graph
        {0: [1,2,3],
        1: [0,4],
        2: [0],
        3: [0],
        4: [1]
    path = [0, 1, 4]
    prev_node = 0,1
    # prev_node to keep track of the node we just came from
    # remove nodes from path when we explore all of its children 

        }


        """
        d = {i:[] for i in range(n)}
        for pair in edges:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0]) # undirected graph
        
        path = set()
        def dfs(node, prev_node):
            if node in path:
                return False 

            path.add(node)
            for preq in d[node]:
                if preq == prev_node:
                    continue
                if not dfs(preq, node):
                    return False
            return True
        return dfs(0, None) and len(path) == n


            

        
        
        


        
        