import functools


def largest_number(nums: list[int]) -> str:
    # ==========================================================================
    # APPROACH: Custom comparator sort
    # ==========================================================================
    # The core question is: given two numbers A and B, which should come first?
    # Answer: whichever produces a bigger number when concatenated.
    # Compare str(A)+str(B) vs str(B)+str(A) — the bigger one wins.
    #
    # Example: A=9, B=34
    #   "9" + "34" = "934"
    #   "34" + "9" = "349"
    #   "934" > "349"  →  9 goes before 34
    #
    # Python's functools.cmp_to_key lets us use a custom comparator with sort().
    # The comparator returns:
    #   -1 if a should come BEFORE b (a+b > b+a)
    #    1 if b should come BEFORE a (b+a > a+b)
    #    0 if they produce the same result either way
    # ==========================================================================

    def comparator(a, b):
        # Concatenate both ways and compare as strings
        # String comparison works here because both sides are same length
        if a + b > b + a:
            return -1  # a goes first — it makes a bigger number
        elif a + b < b + a:
            return 1   # b goes first — it makes a bigger number
        else:
            return 0   # doesn't matter, same result either way

    # Convert all numbers to strings so we can concatenate and compare them
    str_nums = [str(n) for n in nums]

    # Sort using our custom comparator — highest-producing numbers go first
    str_nums.sort(key=functools.cmp_to_key(comparator), reverse=False)

    # Edge case: if the biggest number after sorting is "0", all numbers are 0.
    # Joining them would give "000..." — return "0" instead.
    if str_nums[0] == "0":
        return "0"

    # Join all sorted strings into one final number string
    return "".join(str_nums)
