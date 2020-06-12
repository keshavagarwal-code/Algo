def MaxHeap(lstr):
    if isinstance(lstr, list):
        heap = lstr
    n = len(heap)
    for i in reversed(range(int(n/2))):
        heapify(heap, i, n)
    return heap

def heapify(heap, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = None

    if left < n and heap[left] > heap[i]:
        largest = left
    if right < n and heap[right] > heap[left] and heap[right] > heap[i]:
        largest = right

    if largest:
        heap[largest], heap[i] = heap[i], heap[largest]
        heapify(heap, largest, n)

def sortHeap(lstr):
    for i in reversed(range(len(lstr))):
        lstr[0], lstr[i] = lstr[i], lstr[0]
        for j in range(int(i/2)):
            heapify(lstr, j, i)
    return lstr

def nthElement(collection, k):
    lstr = MaxHeap(collection[:k])
    for i in collection[k:]:
        if i < lstr[0]:
            lstr[0] = i
            for j in reversed(range(int(k/2))):
                heapify(lstr, j, k)
    return lstr

lstr2 = MaxHeap(list(range(100)))
print(nthElement(lstr2, 5))
print(nthElement(lstr2, 3))

