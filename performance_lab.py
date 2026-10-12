# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None #in case there are no numbers

    counts = {}
    best_value = numbers[0]
    best_count = 0

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > best_count:
            best_count = counts[num]
            best_value = num
    return best_value

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - when all elements are unique so it is counted, its hard to predict without the entire list itll beused on.
- Worst-case: O(n) - one pass through the list to count frequencies. The dictionary lookups are O(1) on average.
- Average-case:O(n)
- Space complexity: O(k) where k is the number of unique elements in the list if every value is unique.
- Why this approach? This approach uses a dictionary to count the frequency of each element in a single pass which is efficient and straightforward compared to a loop or any alternative.
- Could it be optimized? Im pretty sure this is the best it gets I know theres certain edge cases where the way the data is interpreted could affect performance, but overall this is efficient.
- Trade offs? The trade-off is that we use extra space to store the counts in the dictionary but this allows us to achieve O(n) time complexity.
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
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) when everything is unique or identical each is only checked once.
- Worst-case: O(n) Set membership and insertion end up being 0(1) on average.
- Average-case: O(n)
- Space complexity:O(n) This is because lists can hold n items when no duplicates are present in the list.
- Why this approach? A hashmap is great when doing constant counting and checking for membership, which helps in efficiently removing duplicates while preserving order in the list.
- Could it be optimized? I have no idea from what I know about this problem, but using a set for membership checks is already quite efficient. I usually would use stack overflow or look at alternative solutions on Leetcode.
- Trade offs? The trade-off is that we use extra space to store the set of seen elements, but this allows us to achieve O(n) time complexity.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs

#tests
print(find_pairs([1, 2, 3, 4], 5))  # Expected output: [(1, 4), (2, 3)]
print(find_pairs([], 6))  # empty list
print(find_pairs([7], 7))  # same pair
print(find_pairs([1, 2, 3, -4], 5))  # Expected output: [(1, 4), (2, 3)]
"""
Time and Space Analysis for problem 3:
- Best-case: O(n^2) because nested loops iterate over all pairs. even with no valid pairing
- Worst-case: O(n^2) because nested loops iterate over all pairs. even with no valid pairing it still checks every element pairing once.
- Average-case: O(n^2) Because its always dependent on the lists length not the values in the lists.
- Space complexity:O(1) only loop counters get used for this which lists can hold up to n/2 for the pairs but still considered constant space relative to the input size.
- Why this approach? It came to me simply because of the wording whenever I think of a problem refering a list and its order doesnt matter I tend to go towards len for counting the size.
- Could it be optimized? Yes 100% I looked at this problem on leetcode and there are more efficient ways using hash sets. Theres also faster ways using two-pointer techniques if the list is sorted.
- Trade-offs: The nested loop approach is simple and uses minimal extra space, but it is not the most efficient in terms of time complexity.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 4  # Initial capacity of the list
    my_list = []  # Start with an empty list

    for i in range(n):
        if len(my_list) == capacity:
            print("List full, resizing from", capacity, "to", capacity * 2)
            capacity = capacity * 2
            new_list = []
            for item in my_list:
                new_list.append(item)
                print("Copying", item)
            my_list = new_list

        my_list.append(i)  # Add the new item to the list
        print("Added", i, "- size: ", len(my_list), "capacity: ", capacity)
    return my_list

print(add_n_items(1)) # just one item, should not trigger resizing
print(add_n_items(10)) # more than initial capacity, should trigger resizing
print(add_n_items(0)) # nothing added, should return an empty list


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Whenever the list reaches its current capacity which for my solution is 4 initially and then doubles each time that the list is full.
- What is the worst-case for a single append? O(n) because it may trigger a resize and copy all existing elements onto a new list which is proportional to the current size of the list.
- What is the amortized time per append overall? O(1) because the appends with the resizing cost are spread out over multiple operations so its not very time intensive. The actual copies of the list are what are expensive but they dont happen often.
- Space complexity: O(n) because the list grows to hold all n elements, and during resizing theres two lists in the memory for a short period while copying and updating occurs simultaneously.
- Why does doubling reduce the cost overall? Because the list holds the time as n and during resizing two lists are held in the memory for while copying and updating occurs, but the cost is spread out over multiple appends, making the amortized cost low.
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
    # Your code here
    pass

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
