import random

#Insertion sort from Zenva on YouTube
def main6_insertion_sort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1

        while j >= 0 and array[j] > current_element:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_element

    return array

#Merge sort modified from FelixTechTips
def main6_merge_sort(array):
    if len(array) <= 1:
        return array

    left = main6_merge_sort(array[:len(array)//2])
    right = main6_merge_sort(array[len(array)//2:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main6_tim_sort(array, k):
    if len(array) <= k:
        return main6_insertion_sort(array)

    left = main6_tim_sort(array[:len(array)//2], k)
    right = main6_tim_sort(array[len(array)//2:], k)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

#question 5 helper functions

#generates an array of size n
def generate_array(n):
    g_array = []
    for _ in range(n):
        g_array.append(random.randint(1, 1000))
    return g_array

#verifies an array is sorted (idk if necessary, the sorting algorithms are assumed to work anyway)
def verify_sorted(test_array):
    prev_val = 0
    for i in range(len(test_array)):
        if test_array[i] < prev_val:
            return False
        prev_val = test_array[i]
    return True