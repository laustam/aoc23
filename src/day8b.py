from math import lcm

file = open("input/day8", "r")

def lcm_of_list(numbers: list[int]):
    result: int = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

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

start_nodes: list[str] = [start for start in network.keys() if start.endswith('A')]
steps_needed: list[int] = [0] * len(start_nodes)

i = 0
for i in range(len(start_nodes)):
    curr_node = start_nodes[i]
    steps: int = 0

    while not curr_node.endswith('Z'):
        curr_dir: chr = directions[steps % len(directions)]
        curr_node = network.get(curr_node).left if curr_dir == 'L' else network.get(curr_node).right
        steps += 1
    steps_needed[i] = steps

print(lcm_of_list(steps_needed))