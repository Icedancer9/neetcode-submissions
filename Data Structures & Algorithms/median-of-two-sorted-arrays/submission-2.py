class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # [1 2 3 4]
        # [1 6 7 8]

        # [2 3 3 6 9]
        # [1 4 4 8]

        # need to do a binary search based on the info I have available
            # arr1[0] or arr2[0] is the smallest number and
            # arr1[-1] or arr2[-1] is the largest number 
            # len(arr1) + len(arr2) // 2 is the median index 
                # If it is even then I need to find the middle 2 values
                # If it is odd then I need to find middle val
        # I can do binary search if I figure this out 

        
    # log(m) * log(n) 
    # I c

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        m,n = len(nums1), len(nums2)
        lo,hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i 

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1,right2)) / 2
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
                
            