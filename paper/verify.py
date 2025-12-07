N = 7 # or 4 if verifying Partial realizer of B_4 

NOT_FOUND_IDX = -1

def is_subset(A, B):
    return (A | B) == B

def index_in_ple(element, ple):
    for i in range(len(ple)):
        if element == ple[i]:
            return i
    return NOT_FOUND_IDX

def throw_bad_realizer():
    raise Exception(f"Provided set of orders is not a Partial realizer of B_{N}.")

def verify(orders):
    for A in range(1<<N):
        for B in range(1<<N):
            if A == B:
                continue

            found_a_less_b = False
            found_b_less_a = False

            for ple in orders:
                a_idx = index_in_ple(A, ple)
                b_idx = index_in_ple(B, ple)

                if a_idx == NOT_FOUND_IDX or b_idx == NOT_FOUND_IDX: 
                    continue
                elif a_idx == b_idx:
                    throw_bad_realizer()
                elif a_idx < b_idx:
                    found_a_less_b = True
                elif a_idx > b_idx:
                    found_b_less_a = True

            is_a_less_b = is_subset(A, B)
            is_b_less_a = is_subset(B, A)
            is_a_not_comparable_with_b = not is_a_less_b and not is_b_less_a

            if ((is_a_less_b and (not found_a_less_b or found_b_less_a)) or
                (is_a_not_comparable_with_b and not (found_a_less_b and found_b_less_a))):
                throw_bad_realizer()

    print(f"Provided set of orders is a correct Partial realizer of B_{N}.")

orders = [list(map(int, input().split())) for i in range(N)]
verify(orders)