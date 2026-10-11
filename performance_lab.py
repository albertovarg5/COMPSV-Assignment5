
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n), because the dictionary stores counts.
- Why this approach? A dictionary counts each number efficiently.
- Could it be optimized? It is already efficient for general input.
"""

# Tests for problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5]) == 5
assert most_frequent([]) is None
assert most_frequent([2, 2, 4, 4]) in [2, 4]


# 🔍 Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because every item must be checked.
- Worst-case: O(n) on average, assuming efficient set operations.
- Average-case: O(n).
- Space complexity: O(n) for the set and result list.
- Why this approach? The set checks duplicates quickly and the
  list preserves the original order.
- Could it be optimized? The time complexity is already O(n)
  on average. Less memory could be used with a different approach,
  but checking a list of seen values would be slower.
"""

# Tests for problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([3, 2, 1]) == [3, 2, 1]


# 🔍 Problem 3: Return All Pairs That Sum to Target

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number

        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because each number is checked once.
- Worst-case: O(n) on average, assuming efficient set operations.
- Average-case: O(n).
- Space complexity: O(n) for the set and output pairs.
- Why this approach? A set quickly finds the number needed
  to reach the target.
- Could it be optimized? This is faster than checking every
  possible pair, which takes O(n^2) time. The output itself
  also requires memory.
"""

# Tests for problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert find_pairs([], 5) == []
assert find_pairs([1, 2, 3], 10) == []
assert set(find_pairs([1, 4, 6, 9], 10)) == {(1, 9), (4, 6)}


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

def add_n_items(n):
    if n < 0:
        raise ValueError("n cannot be negative")

    capacity = 2
    items = [None] * capacity
    size = 0

    print(f"Starting capacity: {capacity}")

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_items = [None] * new_capacity

            for i in range(size):
                new_items[i] = items[i]

            items = new_items
            capacity = new_capacity

            print(f"Resized to capacity: {capacity}")

        items[size] = number
        size += 1

    print(f"Items added: {size}")
    return items[:size]


"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list reaches its capacity.
- Worst-case for a single append: O(n), when all existing
  elements must be copied during resizing.
- Amortized time per append: O(1), because resizing happens
  only occasionally.
- Space complexity: O(n) for storing the elements.
- Why does doubling reduce the cost overall? It creates extra
  space so the list does not need to resize after every append.
"""

# Tests for problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

try:
    add_n_items(-1)
    assert False, "Expected ValueError for negative input"
except ValueError:
    pass


# 🔍 Problem 5: Compute Running Totals

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because every number must be processed.
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) for the new result list.
- Why this approach? Keeping a running sum avoids recalculating
  the sum of all previous numbers each time.
- Could it be optimized? Time is already O(n). Returning a new
  list requires O(n) memory because the output must be stored.
"""

# Tests for problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []
assert running_total([5]) == [5]
assert running_total([-1, 2, -3]) == [-1, 1, -2]
assert running_total([0, 0, 0]) == [0, 0, 0]


# Optimization comparison for Problem 3:
# A simple solution could check every pair using two loops.
# That takes O(n^2) time. The optimized solution above uses a
# set and takes O(n) expected time, but uses O(n) extra space.
# This trades additional memory for faster performance.

print("All tests passed!")

