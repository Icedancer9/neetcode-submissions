class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS from the treasurechest

        # find treasurechest

        rows = len(grid)
        cols = len(grid[0])
        # now do BFS from this coordinate, converting every val > 0 
        # to be the number of steps in bfs

        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        step = 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
            
                for pair in [[1,0],[-1,0],[0,1],[0,-1]]:
                    new_r = r + pair[0]
                    new_c = c + pair[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 2147483647:
                        q.append((new_r,new_c))
                        grid[new_r][new_c] = min(step, grid[new_r][new_c])
            step += 1

                


        


        