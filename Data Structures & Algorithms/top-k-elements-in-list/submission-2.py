class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return Answer.answer(nums, k)


class Answer:
    def answer(nums: List[int], k: int) -> List[int]:
        #
        # [2, 3]
        ans_array = []

        # Get the count of each elem
        # {1:1, 2:2, 3:3}
        # Count backwards based on maximum frequency of each number, populating ans_array
        # Once ans_array is populated all the way, then you can return answer 

        # max_frequency of nums_1 = (MAX(count(nums)) - MAX(count(all_other_nums)))


        # [[1],[2],[3],[],[],[]]
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        freq_array = [list() for i in range(len(nums))]

        for key_num in d:
            num_frequency = d[key_num] - 1
            freq_array[num_frequency].append(key_num)
        
        for i in range(len(freq_array) - 1, -1, -1):
            while freq_array[i]:
                ans_array.append(freq_array[i].pop())
                if len(ans_array) == k:
                    return ans_array
            


        

        


        



        
        