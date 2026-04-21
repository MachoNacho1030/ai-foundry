def single_number(nums: list[int]) -> int:
    # start with 0 — XOR-ing anything with 0 returns that thing unchanged
    result = 0

    # XOR every number in the array into result
    # pairs cancel each other out (n ^ n = 0)
    # the lone number has nothing to cancel with, so it survives
    for num in nums:
        result ^= num

    return result
