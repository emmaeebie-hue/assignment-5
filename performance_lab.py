# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None 
    
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because every number must be checked to determine which appears most frequently.
- Worst-case: O(n), because the function processes every number and updates the dictionary.
- Average-case: O(n), assuming dictionary operations take O(1) time on average.
- Space complexity: O(n), because the dictionary can store up to n distinct numbers.
- Why this approach? A dictionary efficiently counts how many times each number appears, avoiding 
the need to repeatedly compare every number against every other number.
- Could it be optimized? The solution is already efficient for a general unsorted list. If the 
input were already sorted, a different approach could count consecutive occurrences using O(1) 
auxiliary space.
- Trade-offs: The dictionary makes counting faster, but it requires additional memory. A lower-memory
 approach could take longer to run, so the best choice depends on whether time or memory is more 
 important.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

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
- Best-case: O(n), because every element must be checked at least once, even if there are no 
duplicates.
- Worst-case: O(n), because every element is processed, with set lookups and insertions taking
 O(1) time on average.
- Average-case: O(n), because each element is checked and added to the set and result list at 
most once.
- Space complexity: O(n), because the set and result list can each store up to n elements.
- Why this approach? A set allows efficient duplicate checking, while a separate list preserves 
the original order of the elements.
- Could it be optimized? The solution is already efficient for preserving order. Using a dictionary 
to track seen values would have similar time and space complexity.
- Trade-offs: The set requires additional memory, but it avoids repeatedly searching the result 
list for duplicates. Checking the result list directly would use less extra storage but could 
take O(n^2) time in the worst case.
- Optimization comparison: A simpler approach could check whether each number is already in the 
result list, but list membership can take O(n) time per check, resulting in O(n²) worst-case time 
overall. Using a set for duplicate checking reduces the average overall time to O(n), while preserving 
the original order with the result list. The trade-off is O(n) additional space for the set and result list.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because every number must be processed even when no pairs are found.
- Worst-case:  O(n), because each number requires one set lookup and insertion, assuming
 average O(1) set operations.
- Average-case: O(n), because the function processes each number once and uses a set to 
check for its complement.
- Space complexity: O(n), because the set can store up to n numbers and the pairs list 
can store up to n/2 pairs.
- Why this approach? A set allows efficient lookups for the number needed to reach the 
target, avoiding nested loops that compare every possible pair.
- Could it be optimized? The solution is already efficient in time for this problem. 
Space usage could potentially be reduced by changing how pairs are stored or returned, 
depending on the requirements.
- Trade-offs: The set requires additional memory, but it reduces the time needed to find 
pairs. A nested-loop approach would use less auxiliary memory but could take O(n^2) time.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    items = []

    for number in range(n):
        if len(items) == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = []

            for i in range(len(items)):
                new_items.append(items[i])

            items = new_items
            capacity = new_capacity

        items.append(number)

    return items


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizing occurs when the number of elements reaches the current 
capacity. The capacity doubles each time, such as from 2 to 4 and from 4 to 8.
- What is the worst-case for a single append? A resize can take O(n) time because a new list is 
created and the existing elements are copied into it. Most appends take O(1) time when no resize
 is needed.
- What is the amortized time per append overall? O(1), because doubling the capacity makes 
expensive resizing operations infrequent. Across n appends, the total resizing and copying 
work would be O(n).
- Space complexity: O(n), because the function stores n elements in the list. In a real resizing
 implementation, extra temporary memory may be needed while copying elements.
- Why does doubling reduce the cost overall? Doubling provides room for multiple future elements,
 so the list does not need to resize after every append.

"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because every element must be processed to calculate its running total.
- Worst-case: O(n), because the function processes every element once.
- Average-case: O(n), because each element requires one addition and one append operation.
- Space complexity: O(n), because the result list stores one running total for each input element.
- Why this approach? Keeping a running sum avoids recalculating the sum of all previous elements for
 every position, making the solution efficient and easy to understand.
- Could it be optimized? The time complexity is already O(n), which is optimal because every element 
must be processed. The additional space could be reduced by modifying the original list instead of
 returning a new list, but that would change the input.
 - Trade-offs: Returning a new list preserves the original input but requires O(n) additional memory.
   Modifying the original list could save the extra list allocation, but it would change the user's data.
"""

# Tests for Problem 1
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected: 3
print(most_frequent([5, 5, 5, 5]))            # Expected: 5
print(most_frequent([7]))                    # Expected: 7
print(most_frequent([1, 2]))                 # Expected: 1 or 2
print(most_frequent([]))                     # Expected: None

# Tests for Problem 2
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected: [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1, 1]))        # Expected: [1]
print(remove_duplicates([3, 2, 1]))           # Expected: [3, 2, 1]
print(remove_duplicates([]))                  # Expected: []
print(remove_duplicates([8]))                 # Expected: [8]

# Tests for Problem 3
print(find_pairs([1, 2, 3, 4], 5))  # Expected: [(1, 4), (2, 3)]
print(find_pairs([1, 2, 3, 4], 10)) # Expected: []
print(find_pairs([-2, -1, 1, 2], 0)) # Expected: [(-1, 1), (-2, 2)] or equivalent
print(find_pairs([], 5))             # Expected: []
print(find_pairs([7], 14))            # Expected: []

# Tests for Problem 4
print(add_n_items(0))  # Expected: []
print(add_n_items(2))  # Expected: [0, 1], no resize
print(add_n_items(3))  # Expected: resize from 2 to 4
print(add_n_items(6))  # Expected: resize from 2 to 4, then 4 to 8

# Tests for Problem 5
print(running_total([1, 2, 3, 4]))  # Expected: [1, 3, 6, 10]
print(running_total([5, -2, 3]))    # Expected: [5, 3, 6]
print(running_total([]))             # Expected: []
print(running_total([7]))            # Expected: [7]
print(running_total([0, 0, 0]))      # Expected: [0, 0, 0]