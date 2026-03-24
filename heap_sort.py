def _sift_down(items, start, end, compare):
    root = start
    while True:
        child = (2 * root) + 1
        if child > end:
            return

        swap = root
        if compare(items[swap], items[child]) < 0:
            swap = child

        right = child + 1
        if right <= end and compare(items[swap], items[right]) < 0:
            swap = right

        if swap == root:
            return

        items[root], items[swap] = items[swap], items[root]
        root = swap


def heap_sort(items, compare):
    count = len(items)
    start = (count - 2) // 2
    while start >= 0:
        _sift_down(items, start, count - 1, compare)
        start -= 1

    end = count - 1
    while end > 0:
        items[end], items[0] = items[0], items[end]
        end -= 1
        _sift_down(items, 0, end, compare)
