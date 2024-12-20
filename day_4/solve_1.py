import timeit
import pprint

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test_answer = 18

data: str = ''
with open('.\\day_4\\data.txt', 'r') as f:
    data = f.read()

def transpose(l: list) -> list:
    return [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]

def l2str(l: list[str]) -> str:
    return ''.join(l)

def diag_flatten(matrix: list[list]) -> list:
    num_rows: int = len(matrix)
    num_cols: int = len(matrix[0])
    result = []
    for line in range(1, num_rows + num_cols):
        start_col = max(0, line-num_rows)
        count = min(line, (num_cols - start_col), num_rows)
        sublist = []
        for j in range(0, count):
            sublist.append(matrix[min(num_rows, line) - j - 1][start_col + j])
        result.append(sublist)
    return result

def countXMAS(l: list[str]) -> int:
    as_str = l2str(l)
    return as_str.count('XMAS') + as_str[::-1].count('XMAS')

def solve(data: str):
    lines: list[str] = data.splitlines()
    data_matrix: list[list[str]] = [list(line.rstrip()) for line in lines] 

    result = 0
    # rows
    for row in data_matrix:
        result += countXMAS(row)
    diags = diag_flatten(data_matrix)
    # diags
    for diag in diags:
        result += countXMAS(diag)
    # other diags
    diags = diag_flatten(data_matrix[::-1])
    for diag in diags:
        result += countXMAS(diag)
    data_matrix_t = transpose(data_matrix)
    # cols
    for col in data_matrix_t:
        result += countXMAS(col)

    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")