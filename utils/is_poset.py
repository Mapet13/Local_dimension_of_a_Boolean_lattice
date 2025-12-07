# extensions = [
#     [0, 8, 1, 9, 2, 3, 11, 4, 6, 7, 12, 14, 13, 15],
#     [0, 8, 5, 12, 13, 2, 10, 6, 14, 3, 7, 11, 15],
#     [0, 10, 4, 12, 14, 1, 9, 11, 5, 13, 15],
#     [4, 2, 6, 1, 3, 5, 7, 8, 9, 10]
# ]

# extensions = [
#     [0, 1, 2, 3, 4, 6, 7, 8, 12, 14, 9], 
#     [0, 5, 8, 9, 13, 2, 3, 7, 10, 11, 15], 
#     [8, 1, 10, 9, 11, 4, 5, 12, 13, 6, 14, 15], 
#     [4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 7, 13]
# ]

# _extensions_4 = [
#     [0, 8, 4, 12, 2, 6, 14, 1, 3, 5, 7, 9], 
#     [0, 10, 1, 9, 11, 4, 5, 12, 13, 7, 15], 
#     [2, 3, 4, 6, 7, 8, 12, 10, 14, 13, 11, 15], 
#     [1, 5, 8, 9, 13, 2, 10, 3, 11, 6, 14]
# ]

_extensions = [
    [0, 4, 2, 6, 1, 3, 5, 7], 
    [0, 1, 4, 5, 7,], 
    [0, 2, 3, 4, 6, 7], 
    [1, 5, 2, 3, 6]
]

#_extensions_4 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 9, 15], [0, 4, 8, 12, 2, 6, 10, 14, 1, 3, 11, 5, 7, 13, 15], [0, 1, 8, 10, 9, 11, 4, 12, 13, 6, 15],  [9, 5, 13, 2, 3, 7, 10, 11, 14]]
#_extensions_4 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 9, 15], [0, 2, 8, 6, 10, 14, 1, 3, 11, 5, 7, 13, 15], [0, 8, 4, 12, 1, 9, 5, 13, 2, 3, 7, 10, 11, 14, 15], [10, 9, 11, 4, 12, 13, 6],]

# _extensions = [
#    [0, 1, 2, 3, 4, 5, 6, 7], [0, 2, 4, 6, 1, 3, 5, 7], [0, 1, 4, 5, 2, 3, 6, 7]
# ]

# extensions = [
#     [0, 1, 16, 17, 2, 3, 19, 4, 5, 6, 7, 20, 21, 22, 23, 8, 12, 14, 9, 13, 15, 24, 27, 28, 30], 
#     [0, 4, 5, 8, 9, 13, 2, 6, 3, 7, 10, 11, 14, 15, 16, 20, 24, 18, 26, 28, 30, 19, 23, 25, 29], 
#     [0, 18, 8, 1, 10, 24, 26, 9, 11, 25, 27, 4, 20, 5, 21, 12, 13, 29, 6, 7, 14, 15, 22, 23, 31], 
#     [4, 12, 20, 2, 18, 28, 6, 22, 10, 26, 14, 30, 1, 3, 5, 9, 11, 7, 13, 15, 17, 25, 27, 21, 29], 
#     [8, 12, 16, 24, 1, 17, 21, 25, 28, 29, 2, 3, 18, 22, 19, 23, 10, 11, 26, 30, 27, 31]
# ]

# extensions = [[6, 8, 14, 5, 7, 13, 15, 16, 18, 20, 22, 23], 
# [0,  1,  4,  17,  5,  21,  12,  9,  13,  24,  28,  25,  29,  2,  3,  10,  11,  18,  19,  26,  27,  6,  22,  7,  23,  14,  30,  31], 
# [0,  16,  2,  18,  4,  6,  20,  22,  1,  3,  5,  7,  17,  21,  19,  23,  8,  10,  12,  14,  9,  11,  15,  24,  28,  26,  30,  25,  29,  27,  31], 
# [0,  4,  8,  12,  16,  20,  24,  28,  2,  10,  18,  26,  6,  14,  30,  1,  9,  13,  3,  11,  15,  17,  25,  21,  29,  19,  27,  31], 
# [0,  2,  1,  8,  10,  3,  9,  11,  16,  24,  17,  25,  26,  19,  27,  4,  20,  12,  28,  22,  30,  5,  7,  21,  23,  13,  29,  15,  31]
# ]

# extensions = [
#  [32, 1, 33, 8, 40, 4, 5, 36, 37, 9, 12, 13, 2, 10, 34, 42, 6, 41, 38, 7, 14, 11, 15, 39, 44, 45, 43, 46, 47, 16, 48, 24, 56, 17, 18, 50, 49, 20, 22, 28, 21, 23, 52, 60, 26, 54, 30, 53, 55, 25, 57, 58, 62, 27, 29, 59, 61, 31, 63, 64, 80, 68, 66, 82, 84, 70, 86, 65, 81, 72, 73, 76, 69, 77, 96, 88, 89, 92, 85, 91, 93, 100, 112, 97, 116, 95, 113, 117, 104, 124, 105, 121, 125, 98, 106, 114, 122, 107, 123, 102, 103, 111, 118, 126, 119, 127],
#  [0, 96, 34, 98, 16, 48, 50, 112, 114, 4, 68, 84, 36, 100, 52, 38, 54, 102, 8, 72, 40, 12, 104, 76, 44, 108, 24, 60, 46, 116, 118, 92, 58, 62, 74, 106, 78, 120, 124, 90, 110, 94, 122, 126, 1, 65, 5, 69, 67, 9, 13, 73, 77, 33, 97, 37, 41, 101, 105, 45, 11, 75, 99, 107, 71, 109, 79, 103, 111, 17, 19, 49, 51, 81, 113, 83, 25, 27, 89, 57, 59, 91, 21, 85, 121, 123, 29, 93, 53, 117, 61, 125, 23, 55, 95],
#  [88, 2, 10, 32, 104, 56, 120, 42, 1, 9, 25, 33, 41, 57, 26, 58, 3, 35, 19, 73, 51, 11, 27, 43, 59, 74, 106, 90, 122, 83, 89, 75, 113, 115, 105, 91, 121, 107, 123, 4, 68, 6, 70, 20, 84, 22, 86, 12, 28, 5, 69, 13, 76, 77, 36, 100, 14, 30, 92, 21, 7, 85, 78, 15, 79, 87, 29, 31, 94, 95, 37, 44, 45, 38, 46, 39, 47, 52, 60, 54, 61, 62, 63, 108, 110, 101, 109, 111, 116, 119, 124, 127],
#  [64, 16, 8, 72, 24, 4, 12, 28, 1, 88, 65, 17, 21, 81, 84, 85, 25, 89, 92, 29, 93, 32, 96, 48, 112, 33, 36, 37, 52, 116, 40, 49, 113, 56, 44, 53, 101, 117, 41, 45, 108, 109, 57, 60, 61, 120, 124, 121, 125, 2, 34, 66, 98, 18, 82, 50, 114, 6, 38, 70, 22, 54, 86, 102, 10, 42, 14, 46, 110, 118, 62, 122, 126, 3, 35, 7, 39, 15, 43, 47, 19, 51, 59, 55, 63, 67, 99, 83, 115, 123, 71, 87],
#  [16, 20, 80, 2, 66, 6, 70, 18, 82, 22, 86, 8, 14, 74, 26, 30, 1, 17, 90, 81, 78, 9, 5, 13, 94, 3, 19, 11, 27, 7, 15, 23, 31, 67, 75, 83, 91, 71, 79, 87, 95, 32, 40, 48, 33, 34, 49, 50, 35, 96, 98, 97, 99, 36, 38, 51, 112, 100, 114, 115, 102, 53, 118, 39, 103, 55, 119, 56, 41, 104, 105, 42, 57, 43, 106, 46, 107, 47, 110, 111, 60, 58, 59, 62, 63, 120, 122, 123],
#  [0, 18, 3, 35, 17, 19, 49, 51, 64, 66, 65, 67, 96, 98, 80, 82, 81, 83, 97, 99, 4, 5, 7, 68, 69, 20, 21, 71, 23, 37, 85, 87, 113, 39, 53, 55, 101, 103, 115, 116, 118, 117, 119, 8, 12, 72, 76, 24, 28, 9, 73, 13, 88, 77, 10, 29, 89, 93, 40, 44, 121, 45, 14, 61, 108, 124, 42, 26, 109, 125, 30, 11, 15, 27, 31, 58, 47, 63, 74, 90, 78, 94, 126, 75, 91, 79],
#  [0, 72, 65, 73, 68, 76, 69, 77, 32, 97, 100, 101, 104, 108, 105, 2, 34, 66, 10, 109, 74, 106, 3, 35, 67, 99, 6, 70, 71, 102, 78, 103, 43, 75, 79, 110, 107, 111, 16, 18, 80, 48, 50, 82, 112, 114, 20, 84, 22, 86, 52, 24, 54, 88, 117, 56, 115, 23, 87, 119, 25, 120, 28, 92, 125, 26, 90, 30, 94, 126, 31, 95, 127]
#  ]

#extensions = [[0, 1, 2, 3, 16, 17, 19, 4, 5, 20, 6, 7, 21, 22, 23, 32, 38, 35, 54, 64, 96, 51, 39, 55, 81, 66, 67, 83, 68, 70, 113, 101, 117, 71, 102, 99, 103, 86, 87, 115, 118, 119, 8, 10, 24, 26, 12, 14, 30, 9, 11, 13, 15, 72, 88, 74, 73, 75, 89, 76, 78, 77, 79, 27, 91, 92, 94, 93, 95, 40, 42, 104, 56, 106, 58, 41, 105, 43, 107, 123, 44, 108, 46, 45, 47, 109, 111, 60, 126, 61, 127], [0, 32, 64, 96, 4, 20, 48, 80, 84, 112, 1, 33, 65, 17, 5, 21, 97, 49, 69, 113, 85, 36, 100, 52, 116, 37, 53, 8, 40, 9, 41, 12, 24, 28, 13, 25, 56, 57, 72, 101, 29, 104, 73, 105, 120, 89, 121, 44, 45, 60, 61, 76, 92, 108, 77, 109, 93, 124, 117, 125, 2, 18, 6, 22, 3, 19, 7, 23, 10, 34, 42, 26, 11, 14, 66, 74, 67, 46, 75, 50, 70, 78, 15, 58, 79, 35, 82, 54, 98, 106, 114, 47, 111, 86, 27, 30, 31, 62, 63, 90, 122, 94, 126, 83, 87, 119, 127], [8, 40, 1, 10, 9, 33, 35, 41, 16, 17, 48, 25, 11, 49, 18, 57, 64, 65, 80, 112, 43, 81, 19, 51, 73, 97, 67, 99, 105, 75, 107, 27, 59, 83, 90, 113, 89, 121, 91, 115, 123, 4, 20, 5, 12, 28, 13, 21, 29, 6, 7, 14, 15, 22, 23, 68, 69, 77, 84, 93, 87, 79, 30, 94, 31, 95, 36, 52, 100, 37, 53, 117, 109, 125, 38, 54, 39, 63, 102, 103, 118, 119, 110, 126, 127], [0, 4, 8, 12, 2, 6, 10, 14, 1, 3, 5, 9, 11, 7, 13, 15, 64, 66, 73, 69, 76, 74, 67, 75, 77, 70, 78, 71, 79, 32, 33, 96, 104, 97, 34, 105, 36, 100, 42, 44, 108, 37, 45, 101, 38, 98, 106, 109, 99, 39, 46, 43, 107, 47, 102, 103, 110, 111, 16, 17, 18, 19, 20, 21, 22, 23, 48, 50, 24, 52, 54, 80, 49, 112, 82, 114, 84, 116, 81, 53, 118, 83, 85, 117, 51, 55, 115, 87, 119, 25, 28, 26, 29, 31, 56, 58, 57, 88, 120, 59, 90, 122, 121, 123, 62, 63, 92, 124, 127], [0, 16, 2, 66, 34, 98, 18, 50, 82, 114, 8, 72, 24, 88, 10, 26, 74, 90, 40, 104, 42, 56, 58, 106, 120, 122, 4, 68, 20, 6, 22, 12, 70, 86, 28, 76, 14, 92, 78, 36, 52, 38, 54, 44, 46, 100, 102, 108, 110, 30, 94, 116, 60, 124, 62, 118, 126, 1, 9, 17, 3, 19, 25, 11, 27, 5, 7, 13, 15, 21, 23, 29, 31, 33, 41, 35, 49, 37, 57, 53, 55, 45, 59, 47, 61, 63, 65, 97, 67, 73, 69, 77, 105, 109, 71, 75, 79, 103, 81, 85, 111, 89, 93, 113, 117, 119, 125, 91, 95, 127], [24, 28, 25, 29, 26, 30, 27, 31, 32, 48, 34, 50, 40, 56, 42, 58, 36, 52, 41, 51, 37, 53, 43, 59, 44, 60, 46, 62, 39, 45, 55, 61, 47, 63, 64, 80, 96, 112, 65, 68, 100, 69, 72, 104, 88, 120, 66, 98, 82, 114, 74, 106, 122, 84, 121, 99, 115, 107, 91, 123, 85, 76, 116, 108, 101, 124, 70, 78, 110, 86, 125, 71, 95], [68, 65, 72, 16, 80, 84, 81, 88, 89, 85, 2, 92, 93, 18, 82, 90, 86, 3, 71, 94, 83, 91, 87, 95, 32, 48, 33, 49, 57, 96, 112, 34, 98, 35, 50, 114, 120, 122, 60, 116, 124, 61, 38, 62, 102, 110, 118, 126, 39, 97, 101, 113, 121, 125, 43, 99, 107, 103, 111, 51, 115, 59, 123, 55]]


N = 3

def is_subset(A, B):
    return (A | B) == B

def inx(a, le):
    for i in range(len(le)):
        if a == le[i]:
            return i
    return -1

def to_list(a, n):
    pows = [1 << i for i in range(n)]

    result = []
    for i in range(n):
        if a & pows[i] != 0:
            result += [i+1]

    return result


def to_string(a, n, with_gaps = False, mapper = lambda x: x):
    if a == 0:
        return "(/)".center(n)    

    pows = list(map(mapper, [1 << i for i in range(n)]))

    s = ""
    for i in range(n):
        if a & pows[i] != 0:
            s += str(i+1)
        elif with_gaps:
            s += " "
    return s if with_gaps else s.center(n)

def pretty_print(l):
    for i in reversed(range(len(l))):
        print(to_string(l[i]))

def get_max_len(extensions):
    max_len = 0
    for le in extensions:
        if len(le) > max_len:
            max_len = len(le)
    return max_len

def table_print(extensions, n, with_gaps = False, mapper = lambda x: x):
    max_len = get_max_len(extensions)
    for i in reversed(range(max_len)):
        for j in range(len(extensions)):
            if i < len(extensions[j]) and extensions[j][i] & (1 << (n)) == 0:
                text_elem = to_string(extensions[j][i], n)
                if len(text_elem) == 0:
                    text_elem = '--'
                print(to_string(extensions[j][i], n, with_gaps, mapper), end="|")
            else:
                print("".center(n), end="|")
        print()
    
def to_latex(extensions, n):
    line_end = '\\\\\n'
    column_start = "{[}"
    column_end = "{]}"
    column_between = " & "
    space = '\\s'

    num_to_latex = lambda n: "\\" +  str(n)

    result = ""

    max_len = get_max_len(extensions)
    for i in range(max_len):
        for ext_idx in range(len(extensions)):
            if ext_idx > 0:
                result += column_between

            elem_idx = len(extensions[ext_idx]) - i - 1
            if elem_idx < 0:
                for _ in range(n + 2):
                    result += space 
                continue

            result += column_start
        
            nums = to_list(extensions[ext_idx][elem_idx], n)
            for x in range(1, n + 1):
                result += space
                result += num_to_latex(x) if x in nums else space

            result += column_end
        result += line_end

    return result


def is_poset(extensions, n):
    for a in range(1 << n):
        for b in range(1 << n):
            if a == b:
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
            elif is_subset(b, a):
                if not find_higher:
                    raise Exception(f"Not found higher in {bin(a)} {bin(b)}")
                if find_lower:
                    raise Exception(f"Found lower in {bin(a)} {bin(b)}")
            else:
                if not find_higher:
                    raise Exception(f"Not found higher in {bin(a)} {bin(b)}")
                if not find_lower:
                    raise Exception(f"Not found lower in {bin(a)} {bin(b)}")

    print(f"It is a correct partial realizer of B_{n}")

def check_local_dim(extensions, n):
    max_count = -1
    for a in range(1 << n):
        in_ple = []
        count = 0
        idx = 0
        for le in extensions:
            if a in le:
                count += 1
                in_ple += [idx]
            idx += 1
        if count > max_count:
            max_count = count
        #print(to_list(a), in_ple)
    print(f"Local dimension is {max_count}")

def check_without(le_idx, elem_idx):
    extensions_without = []
    for i in range(len(extensions)):
        extensions_without.append([])
        for j in range(len(extensions[i])):
            if i == le_idx and j == elem_idx:
                continue
            extensions_without[i].append(extensions[i][j])

    try:
        is_poset(extensions_without, N)
        elem = bin(extensions[le_idx][elem_idx])
        print(f"It is a correct partial realizer of B_{N} without one element - {extensions[le_idx][elem_idx]}({elem}) in {le_idx}")
    except Exception as _:
        pass

# is_poset(extensions, 3)

# for i in range(len(extensions)):
#     for j in range(len(extensions[i])):
#         check_without(i, j)

# for j in range(len(extensions)):
#     for a in range(1 << N): 
#         if a not in extensions[j]:
#             print(f"Element {bin(a)} is not in extension {j}")


# from math import ceil, log2

# for n in range(2,11):
#     print((n, int(ceil(n/log2(n))))) 

# is_poset(extensions, N)
# check_local_dim(extensions, N)

def rm_last_element(x, n):
    ext = []
    for ple in x:
        a = list(filter(lambda z: z < (1 << n - 1), ple))
        ext.append(a)
    return ext

# ext_6 = rm_last_element(_extensions, 7)
# ext_5 = rm_last_element(ext_6, 6)
# ext_4 = rm_last_element(ext_5, 5)


# table_print(_extensions, 4, True)
# print("----")
# print("----")
# table_print(rm_last_element(_extensions, 4), 3, True)

# is_poset(ext_5, 4)
# check_local_dim(ext_5, 5)
# table_print(ext_5, 5, True)

#print(list(map(lambda a: bin(a), ext_4[0])))


# ext_3 = rm_last_element(extensions, 4)

#is_poset(ext_6, 6)
#check_local_dim(ext_6, 6)
#table_print(ext_4, 4, True)

# print(to_string(1, 7))
# print(to_string(2, 7))
# print(to_string(3, 7))
# print(to_list(1, 7))


#print(to_latex(extensions, N))

# for ext in extensions:
#     print("----------------")
#     pretty_print(ext)
#     print("----------------")

#table_print(extensions, N, True)

is_poset(_extensions, 3)

ext = [[] for i in range(len(_extensions))]

# for x in _extensions[0]:
#     ext[0].append(x)
# for x in _extensions[0]:
#     ext[0].append(x + 8)

for i in range(len(_extensions_4)):
    for x in _extensions[i]:
        ext[i].append(x)
        ext[i].append(x + 8)

is_poset(ext, 4)
print("-----")
table_print(ext, 4, True)
print("-----")



# def map_pows(x):
#     if x == 1:
#         return 4
#     if x == 2:
#         return 2
#     if x == 4:
#         return 1
#     if x == 8:
#         return 8

# table_print(_extensions_4, 4, True )
# print("-----")
# table_print(rm_last_element(_extensions_4, 4), 3, True)
