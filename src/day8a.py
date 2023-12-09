file = open("input/day8", "r")

class Node:
    def __init__(self, left: str, right: str) -> None:
        self.left: str = left
        self.right: str = right

network: dict[Node] = {}
directions: str = file.readline().strip()
file.readline()

for line in file:
    node: str = line.split('=')[0].strip()
    left, right = [child.strip() for child in line.split('=')[1].strip().strip('(').strip(')').split(',')]
    network[node] = Node(left, right)

curr_node: str = "AAA"
steps: int = 0

while curr_node != "ZZZ":
    curr_dir: chr = directions[steps % len(directions)]
    curr_node = network.get(curr_node).left if curr_dir == 'L' else network.get(curr_node).right
    steps += 1

print(steps)