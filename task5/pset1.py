
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
        print(arr)

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r
    print(arr)
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


# Function to build a Max-Heap from the given array


def buildHeap(arr, n):
    # Index of last non-leaf node
    startIdx = n // 2 - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)


def printHeap(arr, n):
    print("Array representation of Heap is:")

    for i in range(n):
        print(arr[i], end=" ")
    print()



if __name__ == '__main__':

    arr = [81, 13, 77, 24, 35, 61, 48, 3, 23, 87, 92, 95, 74, 57, 99, 86, 28, 15, 55, 7, 51]
    n = len(arr)

    buildHeap(arr, n)

    printHeap(arr, n)

