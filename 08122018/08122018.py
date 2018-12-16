from collections import deque

class Node(object):
    def __init__(self):
        self._children = []
        self._metadatas = []

    def add_child(self, child):
        self._children.append(child)

    def add_metadata(self, metadata):
        self._metadatas.append(metadata)

    def cksum(self):
        cksum = 0
        for child in self._children:
            cksum += child.cksum()
        return cksum + sum(self._metadatas)

    def value(self):
        value = 0
        if not self._children:
            value = self.cksum()
        else:
            for metadata in self._metadatas:
                metadata -= 1
                if metadata < len(self._children):
                    value += self._children[metadata].value()
        return value

def parse_data_queue(data_queue):
    node = Node()
    node_count = data_queue.popleft()
    metadata_count = data_queue.popleft()

    while node_count:
        node.add_child(parse_data_queue(data_queue))
        node_count -= 1

    while metadata_count:
        node.add_metadata(data_queue.popleft())
        metadata_count -= 1

    return node

def part1(data_queue):
    data_queue = deque(data_queue)
    node = parse_data_queue(data_queue)
    print(node.cksum())

def part2(data_queue):
    data_queue = deque(data_queue)
    node = parse_data_queue(data_queue)
    print(node.value())

def main():
    with open("input", "r") as f:
        data_array = f.read().split(" ")
        data_array = list(map(int, data_array))

    part1(data_array)
    part2(data_array)

if __name__ == "__main__":
    main()