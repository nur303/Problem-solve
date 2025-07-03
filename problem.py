def heap(arr):
    n = len(arr)

    def heap_property(parent_idx, child_idx):
        if child_idx >= n:
            return True
        if arr[parent_idx] < arr[child_idx]:
            return True
        else:
           arr[parent_idx] > arr[child_idx]
           return False
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2
        return heap_property(child_idx, left_child_idx) and heap_property(child_idx, right_child_idx)
    return heap_property(0, 1) and heap_property(0, 2)
heap_array = [1, 8, 5, 6, 7, 9]
print(heap(heap_array))

non_heap_array = [10, 8, 9, 5, 6, 7]
print(heap(non_heap_array))