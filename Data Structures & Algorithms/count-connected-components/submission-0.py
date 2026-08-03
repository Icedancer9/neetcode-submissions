class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        d = {i:[] for i in range(n)}
        for pair in edges:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])
        
        # {0:[1,2],1:[0],2:[1]} ans = 1
        # {0:[1],1:[0,2],2:[1,3],3:[2],4:[5],5:[4]} ans = 2

        # for each key in d, we do a depth first search and explore all the nodes that we can,
        # from the list in each d[k]
        # We store these nodes in a visited set
        # everytime we see a node not in the visited set, we increment our answer by 1

        seen = set()
        ans = 0
        def dfs(node, prev_node):
            # base case:
                # Terminate the search when node is already in seen or node is previous node
            if node in seen or node == prev_node:
                # prev_node is the node we just came from
                # we need to be aware of this because it is an
                    # undirected graph
                return 
            seen.add(node)
            # now that we've added it to see, lets explore its neighbors
            for neighbor in d[node]:
                dfs(neighbor, node)

            
        
        for k in d.keys():
            if k not in seen:
                ans += 1
                dfs(k,-1)
        return ans 

            


        