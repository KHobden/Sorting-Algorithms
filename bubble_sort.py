# Bubble Sort
# First algorithm script
# Kieran Hobden
# 31-Aug-17

import random

#Define functions
def print_array(arr):
    print (" ".join(str(i) for i in arr))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                x = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = x
        if print_all == "y":
            print("After pass " + str(i + 1) + ":")
            print_array(arr)
    return arr

#Define inputs
arr = []
for x in range(50):
    arr.append(random.randint(0,50))

print_all = "n"

#Input and print data
print_all = input("Would you like all iterations displayed? (y/n)")
print("Initial Array")
print_array(arr)
bubble_sort(arr)
print("Final Array:")
print_array(arr)
