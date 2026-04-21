from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    # Early exit: if the whole system is net negative, no start can fix it
    # sum(gas) < sum(cost) means we lose more fuel than we gain across all stations
    if sum(gas) < sum(cost):
        return -1

    tank = 0   # running fuel balance as we drive forward
    start = 0  # current candidate for the starting station

    for i in range(len(gas)):
        # At each station: pick up gas[i], burn cost[i] driving to next station
        tank += gas[i] - cost[i]

        # If tank goes negative, station `start` through station `i` are all invalid
        # We gave them every advantage (arrived with surplus) and still ran dry
        # Reset: try starting fresh from the next station
        if tank < 0:
            start = i + 1
            tank = 0

    # If we get here, sum(gas) >= sum(cost) so a solution exists
    # The last candidate standing is the unique valid start
    return start
