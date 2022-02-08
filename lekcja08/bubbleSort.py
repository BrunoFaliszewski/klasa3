# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    print(f"\nBefore first iteration: {arr}")
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"\t\t{j + 1}: {arr}")

        print(f"\nAfter {i + 1} iteration: {arr}")


# Driver code to test above
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print(f"\n\nSorted array is: {arr}")
    # for i in range(len(arr)):
    #     print("% d" % arr[i]),
