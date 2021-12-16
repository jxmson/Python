import random
import time


# Binary search algorithm
# We will prove that binary search is faster than naive search

# naive search: scan entire list and ask if its equal to target
def naive_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# we leverage the fact that our list is sorted in a binary search
def binary_search(lst, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    else:
        return binary_search(lst, target, midpoint + 1, high)


if __name__ == '__main__':
    # l1 = [1, 3, 5, 10, 12]
    # t = 10
    # print(naive_search(l1, t))
    # print(binary_search(l1, t))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for t in sorted_list:
        naive_search(sorted_list, t)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for t in sorted_list:
        binary_search(sorted_list, t)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")