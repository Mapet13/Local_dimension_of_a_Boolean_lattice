from typing import Optional

type Element = list[int]
type Lattice_elements = List[Element]
type Realizer = List[Element]
type Paths_to_find_map = dict[Element, Lattice_elements]

def generate_list_of_elements(n: int) -> Lattice_elements:
    result = [[]]
    for i in range(n):
        to_append = []
        for x in result:
            to_append.append(x + [i])
        result += to_append
    return list(map(frozenset, sorted(result, key=len)))

def is_subset(a: Element, b: Element) -> bool:
    return all([x in b for x in a])



def generate_paths_to_find_map(lattice: Lattice_elements) -> Paths_to_find_map:
    paths_to_find = {}
    for a in lattice:
        to_find = []
        for b in lattice:
            if a == b: continue
            if not is_subset(b, a):
                to_find.append(b)
        paths_to_find.update({a : to_find})
    return paths_to_find

def find_smallest_not_satisfied_element(paths_map: Paths_to_find_map) -> Optional[Element]:
    for element, paths in paths_map.items():
        if len(paths) == 0:
            return element
    return None

def count_usage(a: Element, realizer: Realizer) -> int:
    usage = 0
    for ple in realizer:
        for x in ple:
            if a == x: usage += 1  
    return  usage

def find_smallest_not_satisfied_element(paths_map):
    for element, paths in paths_map.items():
        if len(paths) == 0:
            return element
    return None

def find_realizer(n: int) -> Realizer:
    realizer = []

    elements = generate_list_of_elements(n)
    paths_to_find = generate_paths_to_find_map(elements)
    next_to_start = find_smallest_not_satisfied_element(paths_to_find)
    
    while(next_to_start is not None):
        possible_paths = []
        print(next_to_start, paths_to_find)

        visited = []
        current_path = []
        current_element = next_to_start

        while current_element is not None:
            x = current_element
            current_path.append(current_element)
            for a in current_path:
                if a != x:
                    paths_to_find[a].remove(x) 
            current_element = get_next(current_element, paths_to_find, current_path)
            
        
        realizer += current_path
        next_to_start = find_smallest_not_satisfied_element(paths_to_find)


    return realizer


print(find_realizer(2))