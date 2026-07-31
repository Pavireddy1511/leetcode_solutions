class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [0] * len(nums1)
        s1 = []
        hm = {}

        # Use stack and fill hashmap from nums2
        for n in nums2:
            while s1 and n > s1[-1]:
                hm[s1.pop()] = n
            s1.append(n)

        # Build result using hashmap
        idx = 0
        for k in nums1:
            if hm.get(k):
                res[idx] = hm.get(k)
            else:
                res[idx] = -1
            idx += 1

        return res