from collections import deque


def reverse_first(queue, k):
    queue = deque(queue)

    if k < 0 or k > len(queue):
        raise ValueError("k must be between 0 and the queue length")

    stack = []

    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return list(queue)


print(reverse_first([10, 20, 30, 40, 50], k = 3))
print(reverse_first([1, 2, 3, 4], k = 2))
