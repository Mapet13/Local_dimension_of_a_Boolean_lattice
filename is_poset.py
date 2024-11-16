extensions = [
 [4, 2, 6, 1, 3, 5, 7, 8, 9, 10],
 [0, 8, 1, 9, 2, 3, 11, 4, 6, 7, 12, 14, 13, 15],
 [0, 8, 5, 12, 13, 2, 10, 6, 14, 3, 7, 11, 15],
 [0, 10, 4, 12, 14, 1, 9, 11, 5, 13, 15]
]

N = 4

def is_subset(A, B):
    return (A | B) == B

def inx(a, le):
    for i in range(len(le)):
        if a == le[i]:
            return i
    return -1


def is_poset(extensions, n):
    for a in range(1 << n):
        for b in range(1 << n):
            if a >= b:
                continue
            find_lower = False
            find_higher = False
            for le in extensions:
                a_idx = inx(a, le)
                b_idx = inx(b, le)
                if a_idx != -1 and b_idx != -1 and a_idx < b_idx:
                    find_lower = True
                if a_idx != -1 and b_idx != -1 and a_idx > b_idx:
                    find_higher = True
            if is_subset(a, b):
                if not find_lower:
                    raise Exception(f"Not found lower in {bin(a)} {bin(b)}")
                if find_higher:
                    raise Exception(f"Found higher in {bin(a)} {bin(b)}")
            else:
                if not find_higher:
                    raise Exception(f"Not found higher in {bin(a)} {bin(b)}")
                if not find_lower:
                    raise Exception(f"Not found lower in {bin(a)} {bin(b)}")

    print(f"It is a proper partial realizer of B_{n}")

def check_local_dim(extensions, n):
    max_count = -1
    for a in range(1 << n):
        count = 0
        for le in extensions:
            if a in le:
                count += 1
        if count > max_count:
            max_count = count
    print(f"Local dimension is {max_count}")


is_poset(extensions, N)
check_local_dim(extensions, N)
