from functools import cmp_to_key

import sage.libs.ecl

from sat_vars import construct_variable_map, VarType, get_boolean_graph


sage.libs.ecl.ecl_eval("(ext:set-limit 'ext:heap-size 0)")


def to_str(x):
    str = ""

    current_letter = "a"
    current_number = 1

    while current_number <= x:
        if x & current_number:
            str += current_letter
        current_number *= 2
        current_letter = chr(ord(current_letter) + 1)

    has_any_letter = any(c.isalpha() for c in str)
    return str if has_any_letter else "(/)"


def recover_order(values, variables, n, lin_ext_idx):
    is_used = lambda x: values[variables(VarType.IsUsed, x, lin_ext_idx)] > 0
    ordering = list(filter(is_used, [e for e in range(1 << n)]))

    def Compare(a, b):
        was_reversed = False
        if a > b:
            a, b = b, a
            was_reversed = True
        is_lower = values[variables(VarType.IsLess, a, b, lin_ext_idx)]
        is_higher = values[variables(VarType.IsMore, a, b, lin_ext_idx)]

        multiplier = 1 if not was_reversed else -1
        if is_lower:
            return -1 * multiplier
        if is_higher:
            return 1 * multiplier
        else:
            raise Exception("That should not happend!")

    return sorted(ordering, key=cmp_to_key(Compare))


def to_list(data):
    return [0] + sum(
        list(map(lambda x: x.strip().split(" ")[1:], data.split("\n"))), []
    )


def to_map(list_data):
    values = {i: int(list_data[i]) > 0 for i in range(len(list_data))}
    values.update({-i: not (int(list_data[i]) > 0) for i in range(len(list_data))})
    return values


def to_string(a, n, with_gaps=False):
    if a == 0:
        return "(/)".center(n)

    pows = [1 << i for i in range(n)]

    s = ""
    for i in range(n):
        if a & pows[i] != 0:
            s += str(i + 1)
        elif with_gaps:
            s += " "
    return s if with_gaps else s.center(n)


def get_only_data_lines(input: str) -> str:
    return "\n".join(line for line in input.splitlines() if line.startswith("v"))


def parse_solution(n, le_count, data, should_to_string=False):
    variables = construct_variable_map(
        sorted(get_boolean_graph(n).vertices()), le_count
    )
    values = to_map(to_list(get_only_data_lines(data)))
    result = [recover_order(values, variables, n, j) for j in range(le_count)]
    if should_to_string:
        return [list(map(to_str, x)) for x in result]
    return result


def get_max_len(extensions):
    max_len = 0
    for le in extensions:
        if len(le) > max_len:
            max_len = len(le)
    return max_len


def table_print(extensions, n, with_gaps=False):
    max_len = get_max_len(extensions)
    for i in reversed(range(max_len)):
        for j in range(len(extensions)):
            if i < len(extensions[j]) and extensions[j][i] & (1 << (n)) == 0:
                text_elem = to_string(extensions[j][i], n)
                if len(text_elem) == 0:
                    text_elem = "--"
                print(to_string(extensions[j][i], n, with_gaps), end="|")
            else:
                print("".center(n), end="|")
        print()


if __name__ == "__main__":
    file = "636_s.txt"
    n = 6
    ldim = 3
    le_count = 6

    data = open(file, "r").read()

    result = parse_solution(
        n=n,
        le_count=le_count,
        data=data,
        should_to_string=False,
    )

    # table_print(result, n, True)
    print(result)
