#Merge Sort
#Kieran Hobden
#18-Sep-'19

#Cycles through both lists simultaneously, returning the lower value of any two selected elements
def compare(left, right):

    #Indices cycle through left and right lists
    i, j = 0, 0
    result = []

    #Increase the index only when the selected element is smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #Add on the remaining terms to the end of the result
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(unsorted):
    #Return the list if it is indivisible as it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    #Recursively apply merge_sort and compare to create a diamond-shaped tree diagram
    mid = int(len(unsorted)/2)
    left = merge_sort(unsorted[:mid])
    right = merge_sort(unsorted[mid:])

    return compare(left, right)


unsorted = [4, 2, 6, 5, 1, 9]

print(unsorted)
print(merge_sort(unsorted))
