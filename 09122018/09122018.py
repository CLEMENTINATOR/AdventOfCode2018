import parse
from collections import defaultdict

class DoubleLinkedListNode(object):
    def __init__(self, value):
        self._value = value
        self._previous = self
        self._next = self

    def get_next(self):
        return self._next

    def get_previous(self, count=1):
        if count == 0:
            return self
        else:
            return self._previous.get_previous(count-1)

    def append_node(self, node):
        self._next._previous = node
        node._next = self._next
        node._previous = self
        self._next = node

    def remove_node(self):
        next_node = self._next
        previous_node = self._previous
        previous_node._next = next_node
        next_node._previous = previous_node
        self._next = None
        self._previous = None
        return self._value

def part1(player_count, marble_count):
    current_player = 1
    player_score = defaultdict(int)

    marble_circle = DoubleLinkedListNode(0)
    current_marble = marble_circle

    for marble_id in range(1, marble_count):
        if marble_id % 23 != 0:
            new_marble = DoubleLinkedListNode(marble_id)
            current_marble.get_next().append_node(new_marble)
            current_marble = new_marble
        else:
            player_score[current_player] += marble_id
            player_score[current_player] += current_marble.get_previous(7).remove_node()
            current_marble = current_marble.get_previous(6)

        # debug print
        """print("[{}]".format(current_player), end = " ")
        cur_node = marble_circle
        while True:
            if cur_node._value == current_marble._value:
                value_format = "({})"
            else:
                value_format = "{}"

            print(value_format.format(cur_node._value), end=" ")
            cur_node = cur_node._next
            if cur_node == marble_circle:
                break
        print("")
        input()"""

        current_player += 1
        if current_player > player_count:
            current_player = 1

    winning_player = max(player_score, key=lambda k: player_score[k])
    print("{} players; last marble is worth {} points: high score is {}"
        .format(player_count, marble_count ,player_score[winning_player]))


def main():
    with open("input", "r") as f:
        rule = f.read()
        r = parse.parse("{} players; last marble is worth {} points", rule)
        marble_count = int(r[1])
        player_count = int(r[0])
        part1(player_count, marble_count)
        part1(player_count, marble_count*100)

if __name__ == "__main__":
    main()