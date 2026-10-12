class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = l + (r - l) // 2
            if self.try_eat(m, piles, h):
                r = m
            else:
                l = m + 1
        return l

        

    def try_eat(self, eat_speed: int, piles: List[int], max_speed: int):
        total_speed = 0
        for pile in piles:
            total_speed += math.ceil(float(pile)/eat_speed)
            if total_speed > max_speed:
                return False 
        return True 



        



        