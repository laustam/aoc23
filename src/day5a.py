file = open("input/day5", "r")

class Mapping:
    soil: int = None
    fertilizer: int = None
    water: int = None
    light: int = None
    temperature: int = None
    humidity: int = None
    location: int = None

    def __init__(self, seed: int) -> None:
        self.seed:int = seed
    
    def in_range(self, attr_name: str, val_range: range) -> (bool, int):
        attr_val = getattr(self, attr_name)
        if attr_val not in val_range:
            return (False, -1)
        return (True, attr_val - val_range.start)

def put_map(source: str, dest: str, file, mappings: list[Mapping]):
    file.readline()
    while True:
        line: str = file.readline()
        if not line or line == "\n":
            break

        dest_val, source_val, length = [int(val) for val in line.strip().split(" ")]

        for mapping in mappings:
            in_range, offset = mapping.in_range(source, range(source_val, source_val+length))
            if in_range:
                setattr(mapping, dest, dest_val + offset)

    for mapping in mappings:
        source_attr = getattr(mapping, source)
        if not getattr(mapping, dest):
            setattr(mapping, dest, source_attr)
    

mappings: list[Mapping] = []

for initial_seed in file.readline().strip().split(" ")[1:]:
    new_mapping: Mapping = Mapping(int(initial_seed))
    mappings.append(new_mapping)

file.readline()

put_map(source="seed", dest="soil", file=file, mappings=mappings)
put_map(source="soil", dest="fertilizer", file=file, mappings=mappings)
put_map(source="fertilizer", dest="water", file=file, mappings=mappings)
put_map(source="water", dest="light", file=file, mappings=mappings)
put_map(source="light", dest="temperature", file=file, mappings=mappings)
put_map(source="temperature", dest="humidity", file=file, mappings=mappings)
put_map(source="humidity", dest="location", file=file, mappings=mappings)

print(min([mapping.location for mapping in mappings]))