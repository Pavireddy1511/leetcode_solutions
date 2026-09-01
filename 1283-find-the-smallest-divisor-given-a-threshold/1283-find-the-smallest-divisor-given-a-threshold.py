class Solution:
    def smallestDivisor(self, nums, threshold):
        start = 1
        end = max(nums)

        while start <= end:
            mid = start + (end - start) // 2

            if self.shold(mid, nums, threshold) <= threshold:
                end = mid - 1
            else:
                start = mid + 1

        return start

    def shold(self, mid, nums, threshold):
        total = 0

        for num in nums:
            total += (num + mid - 1) // mid

            if total > threshold:
                return total

        return total
        