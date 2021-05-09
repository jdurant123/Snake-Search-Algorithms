import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def put(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def get(self):
        if len(self._queue) < 1:
            return None
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        return len(self._queue) < 1


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.put((1, 2), 1)
    queue.put((3, 4), 3)
    queue.put((2, 3), 2)
    print(queue.get())
    print(queue.get())
    print(queue.empty())
    print(queue.get())
    print(queue.empty())
