class Heap:
    def __init__(self, lstr=None):
        self.heap = []
        if isinstance(lstr, list):
            self.heap = lstr
            self.buildheap()

    def __repr__(self):
        return " ,".join(str(i) for i in self.heap)
    
    def buildheap(self):
        n = len(self.heap)
        for i in range(int(n/2)-1, -1, -1):
            self.heapify(i, n)

    def heapify(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = None
        
        if left < n and self.heap[left] > self.heap[i]:
            largest = left
        if right < n and self.heap[right] > self.heap[i] and self.heap[right] > self.heap[left]:
            largest = right
        
        if largest:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest, n)

    def heapSort(self):
        n = len(self.heap)
        for i in reversed(range(n)):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            for j in range(int(len(self.heap)/2), -1, -1):
                self.heapify(j, i)
        




hp = Heap([5, 3, 16, 2, 10, 14])
print(hp)
hp.heapSort()
print(hp)