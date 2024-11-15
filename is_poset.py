extensions = [
[21, 37, 8, 13, 29, 45, 53, 61, 2, 6, 10, 14, 15, 31],
[0, 4, 1, 5, 2, 12, 9, 10, 3, 11, 13, 14, 7, 15, 32, 36, 33, 37, 40, 44, 41, 45, 34, 42, 38, 46, 35, 43, 39, 47, 16, 20, 17, 21, 48, 24, 56, 52, 28, 60, 49, 25, 57, 61, 18, 50, 26, 22, 54, 19, 51, 23, 55, 58, 30, 62, 27, 59, 63],
[0, 16, 4, 2, 8, 10, 12, 6, 14, 1, 5, 9, 3, 11, 20, 17, 24, 25, 28, 29, 18, 19, 7, 22, 23, 26, 27, 30, 31, 32, 33, 48, 36, 37, 49, 52, 40, 41, 53, 56, 57, 44, 60, 61, 34, 35, 50, 51, 38, 39, 54, 55, 42, 43, 58, 59, 46, 47, 62, 63],
[0, 1, 3, 4, 5, 6, 16, 17, 20, 21, 32, 33, 34, 35, 7, 36, 38, 39, 48, 49, 52, 53, 18, 19, 50, 51, 22, 23, 54, 55, 8, 9, 12, 13, 40, 41, 44, 24, 25, 56, 57, 28, 29, 60, 10, 11, 14, 15, 26, 30, 31, 42, 43, 46, 45, 47, 58, 59, 62, 63],
[0, 4, 8, 12, 32, 36, 40, 44, 16, 20, 24, 28, 48, 52, 56, 60, 2, 6, 34, 38, 42, 46, 18, 22, 26, 30, 50, 54, 58, 62, 1, 5, 33, 37, 9, 13, 41, 45, 17, 21, 25, 29, 49, 53, 57, 61, 3, 7, 11, 15, 35, 39, 43, 19, 23, 47, 27, 31, 51, 55, 59, 63],
[0, 32, 1, 33, 16, 48, 17, 49, 8, 40, 9, 41, 24, 56, 25, 57, 2, 3, 10, 11, 34, 35, 18, 50, 19, 51, 42, 43, 26, 58, 27, 59, 4, 6, 36, 38, 5, 7, 37, 39, 20, 22, 52, 21, 12, 14, 44, 46, 13, 15, 45, 47, 53, 54, 23, 55, 28, 30, 60, 62, 29, 31, 61, 63]
]

N = 6

def is_subset(A, B):
    return (A | B) == B

def inx(a, le):
    for i in range(len(le)):
        if a == le[i]:
            return i
    return -1


for a in range(1 << N):
    for b in range(1 << N):
        if a < b:
            if is_subset(a, b):
                find_lower = False
                find_higher = False
                for le in extensions:
                    a_idx = inx(a, le)
                    b_idx = inx(b, le)
                    if a_idx != -1 and b_idx != -1 and a_idx < b_idx:
                        find_lower = True
                    if a_idx != -1 and b_idx != -1 and a_idx > b_idx:
                        print(a, b, le, "FOUND HIGHER")
                        exit(0)
                        find_higher = True
                if not find_lower:
                    print(bin(a), bin(b), "not found lower")
                if find_higher:
                    print(bin(a), bin(b), "found higher")
            else:
                find_lower = False
                find_higher = False
                for le in extensions:
                    a_idx = inx(a, le)
                    b_idx = inx(b, le)
                    if a_idx != -1 and b_idx != -1 and a_idx > b_idx:
                        find_higher = True
                    if a_idx != -1 and b_idx != -1 and a_idx < b_idx:
                        find_lower = True
                if not find_higher:
                    print(bin(a), bin(b), "not found higher")
                if not find_lower:
                    print(bin(a), bin(b), "not found lower")
        

            