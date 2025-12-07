from ast import Call
from typing import Callable
from from_sat import parse_solution, get_max_len
from singletons_fixtures import From_sat_636


def to_list(a, n: int, mapper: Callable = lambda x: x) -> list[int]:
    pows = [1 << (mapper(i + 1) - 1) for i in range(n)]

    result = []
    for i in range(n):
        if a & pows[i] != 0:
            result += [i + 1]

    return result


def load_colors() -> list[str]:
    colors_cfg_filename = "cell_colors_cfg.txt"
    with open(colors_cfg_filename) as file:
        return [line.rstrip() for line in file]


def get_color_setter(colors: list[str], n: int) -> str:
    return "\\cellcolor{" + colors[n - 1] + "}"


def gen_header(le_count: int) -> str:
    start = """\\begin{table}[]
    \\scriptsize
    \\sffamily
    \\centering
    \\begin{tabular}{|"""
    to_desc = """}\\hline\\rule[-1.5ex]{0pt}{2pt} $L_1$ \\rule{0pt}{3ex}"""
    end = " \\\\"

    cols = "c|" * le_count
    rest_of_desc = ""
    if le_count > 1:
        for i in range(2, le_count + 1):
            rest_of_desc += f"& $L_{i}$"

    return start + cols + to_desc + rest_of_desc + end


def gen_table_end() -> str:
    return """\\hline
    \\end{tabular}
    \\end{table}"""


def to_latex(
    extensions, n: int, with_table: bool = False, mapper: Callable = lambda x: x
) -> str:
    line_end = "\\\\\n"
    column_start = "{[}"
    column_end = "{]}"
    column_between = " & "
    space = "\\s"

    num_to_latex = lambda n: "\\" + str(n)

    result = ""

    colors = load_colors()
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

            nums = to_list(extensions[ext_idx][elem_idx], n, mapper)
            is_singleton = len(nums) == 1

            if is_singleton:
                result += get_color_setter(colors, nums[0])

            for x in range(1, n + 1):
                result += space
                result += num_to_latex(x) if x in nums else space

            result += column_end
        result += line_end

    if with_table:
        return gen_header(le_count) + result + gen_table_end()
    return result


if __name__ == "__main__":
    file = "535_s.txt"
    n = 5
    ldim = 3
    le_count = 5

    data = open(file, "r").read()

    result = parse_solution(
        n=n,
        le_count=le_count,
        data=data,
        should_to_string=False,
    )

    def mapper(n: int) -> int:
        # if n == 3:
        #    return 1
        # if n == 6:
        #    return 4
        # if n == 1:
        #    return 3
        # if n == 5:
        #    return 2
        # if n == 2:
        #    return 6
        # if n == 4:
        #    return 5

        return n

    # latex_table = to_latex(
    #    result,
    #    n,
    #    with_table=True,
    #    mapper=mapper,
    # )

    table =[[6, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 1, 0, 3, 7, 9, 11, 13, 15, 17, 19, 23, 25, 27, 29, 31, 35, 39, 47, 49, 51, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127], [12, 20, 24, 28, 36, 44, 48, 52, 56, 60, 64, 68, 76, 84, 92, 96, 100, 108, 112, 116, 120, 124, 1, 5, 13, 21, 29, 33, 37, 45, 53, 61, 69, 77, 85, 93, 97, 101, 109, 113, 117, 121, 125, 2, 0, 6, 14, 15, 18, 22, 26, 30, 31, 34, 38, 46, 50, 54, 58, 62, 63, 70, 71, 78, 79, 94, 95, 98, 99, 102, 103, 110, 111, 114, 115, 118, 119, 122, 123, 126, 127], [24, 40, 56, 72, 88, 104, 120, 1, 9, 25, 41, 57, 65, 73, 89, 105, 121, 2, 10, 11, 26, 27, 42, 43, 58, 59, 66, 67, 74, 75, 90, 91, 106, 107, 122, 123, 4, 0, 28, 30, 60, 62, 124, 125, 126, 127], [17, 48, 49, 80, 81, 112, 113, 2, 3, 18, 19, 50, 51, 82, 83, 114, 115, 4, 5, 7, 20, 21, 22, 23, 52, 53, 54, 55, 84, 85, 86, 87, 116, 117, 118, 119, 8], [33, 34, 35, 96, 97, 98, 99, 4, 6, 36, 37, 38, 39, 100, 101, 102, 103, 8, 10, 12, 14, 40, 41, 42, 43, 44, 45, 46, 47, 104, 105, 106, 107, 108, 109, 110, 111, 16], [65, 66, 67, 68, 69, 70, 71, 8, 72, 73, 74, 75, 76, 77, 78, 79, 16, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 32], [3, 5, 7, 9, 11, 13, 15, 16, 17, 19, 21, 23, 25, 27, 29, 31, 32, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 64]] 
    latex_table = to_latex(table, 7, with_table=True)

    print(latex_table)
