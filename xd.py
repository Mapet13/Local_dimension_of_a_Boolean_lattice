# from collections import defaultdict
# import copy

# def find_limited_paths(graph, k):
#     paths = []
#     vertex_usage = defaultdict(int)
#     start_usage = defaultdict(int) 
    
#     def dfs(node, path, usage):
#         if vertex_usage[node] >= k:
#             return None
        
#         path.append(node)
#         usage[node] += 1
        
#         paths_from_current = []
#         for neighbor in graph[node]:
#             if neighbor not in path and usage[neighbor] < k:
#                 res_dfs = dfs(neighbor, path[:], copy.deepcopy(usage)) 
#                 if res_dfs is not None:
#                     paths_from_current.append(res_dfs)

#         if len(paths_from_current) == 0:
#             return path
#         return max(paths_from_current, key=len)
    
#     for start in graph:
#         while start_usage[start] < k and vertex_usage[start] < k:
#             result = dfs(start, [], copy.deepcopy(vertex_usage))
#             start_usage[start] += 1
#             if result is not None:
#                 print('---------', result)
#                 for x in result:
#                     vertex_usage[x] += 1
#                 paths.append(result)
    
#     return paths

# k = 2
# paths = find_limited_paths(graph, k)
# for p in paths:
#     print(p)a

def find_all_hamiltonian_paths(graph, start, end):
    # Collect all unique nodes in the graph
    all_nodes = set()
    for node in graph:
        all_nodes.add(node)
        for neighbor in graph[node]:
            all_nodes.add(neighbor)
    total_nodes = len(all_nodes)
    
    # Check if start or end is missing in the graph
    if start not in all_nodes or end not in all_nodes:
        return []
    
    def dfs(current_node, path, visited, all_paths):
        for prev in path:
            if is_subset(current_node, prev):
                return

        visited.add(current_node)
        path.append(current_node)
        
        neighbors = graph.get(current_node, [])
        if current_node == end or len(neighbors) == 0:
            all_paths.append(list(path))
        else:
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor, path, visited, all_paths)
        
        path.pop()
        visited.remove(current_node)
    
    all_paths = []
    dfs(start, [], set(), all_paths)
    return all_paths


def find_smallest_not_satisfied_element(paths_map):
    for element, paths in paths_map.items():
        if len(paths) > 0:
            return element
    return None

def generate_list_of_elements(n):
    result = [[]]
    for i in range(n):
        to_append = []
        for x in result:
            to_append.append(x + [i])
        result += to_append
    return list(map(frozenset, sorted(result, key=len)))

def is_subset(a, b) -> bool:
    return all([x in b for x in a])

def generate_paths_to_find_map(lattice):
    paths_to_find = {}
    for a in lattice:
        to_find = []
        for b in lattice:
            if a == b: continue
            if not is_subset(b, a):
                to_find.append(b)
        paths_to_find.update({a : to_find})
    return paths_to_find

elements = generate_list_of_elements(3)
graph = generate_paths_to_find_map(elements)

paths = find_all_hamiltonian_paths(graph, elements[0], elements[-1])

def count_removed(path):
    result = 0
    prev = []
    for x in path:
        for p in prev:
            if x in graph[p]: 
                result += 1 
        prev.append(x)
    return result


def realizer():
    selected = []
    while True:
        lowest = find_smallest_not_satisfied_element(graph)
        if lowest is None:
            return selected

        # to_include = []
        # for v in graph.keys():
        #     used = False
        #     for u, e in graph.items():
        #         used = True
        #     if not used:
        #         to_include = True


        paths = find_all_hamiltonian_paths(graph, lowest, elements[-1])
        path_gen = max(sorted(paths, key=len, reverse=True), key=count_removed)

        # while len(to_include) == 0:
        #     inc = to_include[0]
        #     path = []

        #     for i in range(len(path_gen)):



            #path_gen = path

        path = path_gen

        if count_removed(path) == 0:
            return selected

        redundant = []
        prev = []
        for x in path:
            done_anything = False
            for p in prev:
                if x in graph[p]:
                    if p in redundant:
                        redundant.remove(p)
                    done_anything = True
                    graph[p].remove(x)
            prev.append(x)
            if not done_anything:
                redundant.append(x)

        selected.append([a for a in path if a not in redundant])

ples = realizer()
for a in ples:
    print(a)
print('====')

def count_occur(x):
    r = 0
    for p in ples:
        if x in p:
            r += 1
    print(r)
    return r

ldim = 0
for x in graph.keys():
    r = count_occur(x)
    if r > ldim:
        ldim = r

print(r)

print('====')
for x in graph.items():
    print(x)

    