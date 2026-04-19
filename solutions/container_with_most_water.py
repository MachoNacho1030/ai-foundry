def max_area(height: list[int]) -> int:
    # Put your left finger on the first stick in the row
    left = 0

    # Put your right finger on the last stick in the row
    right = len(height) - 1

    # You haven't measured any containers yet, so the best is zero
    best = 0

    # Keep going as long as your fingers haven't crossed or met
    while left < right:
        # Count how many spaces apart your two fingers are — that's the container width
        width = right - left

        # The shorter of the two sticks is your wall height
        # Water can't go higher than the shorter stick or it spills over
        current_height = min(height[left], height[right])

        # Multiply width by height to get the water amount
        # If it beats the previous best, save it
        best = max(best, width * current_height)

        # The left stick is shorter — it's the bottleneck
        # Move the left finger inward to look for something taller
        if height[left] < height[right]:
            left += 1
        else:
            # The right stick is shorter (or equal) — it's the bottleneck
            # Move the right finger inward instead
            right -= 1

    # Every worthwhile combination has been checked — return the biggest water amount found
    return best
