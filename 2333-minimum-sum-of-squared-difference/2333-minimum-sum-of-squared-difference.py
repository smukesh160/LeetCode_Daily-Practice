from typing import List


class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:
        differences = [
            abs(first - second)
            for first, second in zip(nums1, nums2)
        ]

        operations = k1 + k2

        if sum(differences) <= operations:
            return 0

        # Find the smallest maximum difference achievable.
        left = 0
        right = max(differences)

        while left < right:
            middle = (left + right) // 2

            required = sum(
                max(difference - middle, 0)
                for difference in differences
            )

            if required <= operations:
                right = middle
            else:
                left = middle + 1

        threshold = left

        # Reduce every difference greater than the threshold.
        used = sum(
            max(difference - threshold, 0)
            for difference in differences
        )
        remaining = operations - used

        answer = sum(
            min(difference, threshold) ** 2
            for difference in differences
        )

        # Use the remaining operations to change threshold into threshold - 1.
        answer -= remaining * (2 * threshold - 1)

        return answer