"""
Trapping Rain Water — LeetCode #42
Wrapped in Solution class for direct LeetCode submission.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        # Can't trap water with fewer than 3 bars
        if len(height) < 3:
            return 0

        left, right = 0, len(height) - 1   # pointers start at each end
        left_max, right_max = 0, 0          # tallest wall seen from each side
        water = 0

        while left < right:
            if height[left] <= height[right]:
                # Left side is the limiting wall
                if height[left] >= left_max:
                    left_max = height[left]  # new tallest left wall, no water here
                else:
                    water += left_max - height[left]  # water fills up to left_max
                left += 1
            else:
                # Right side is the limiting wall
                if height[right] >= right_max:
                    right_max = height[right]  # new tallest right wall, no water here
                else:
                    water += right_max - height[right]  # water fills up to right_max
                right -= 1

        return water
