from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # Always binary search on the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n) // 2

    lo, hi = 0, m

    while lo <= hi:
        # i = how many elements we take from nums1 for the left half
        i = (lo + hi) // 2
        # j = how many elements we take from nums2 for the left half
        j = half - i

        # Edge values at the partition boundary
        left1  = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i]     if i < m else float('inf')
        left2  = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j]     if j < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            # Found the correct partition
            if (m + n) % 2 == 1:
                return float(min(right1, right2))
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            # Took too many from nums1, move left
            hi = i - 1
        else:
            # Took too few from nums1, move right
            lo = i + 1
