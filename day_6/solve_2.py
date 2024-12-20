import timeit
import pprint

from solve_1 import path_length

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
test_answer = 6

data: str = ''
with open('.\\day_6\\data.txt', 'r') as f:
    data = f.read()

# Just put blockers on all possible locations
# and wait for 30 seconds...
def lazy_way(data_matrix: list[str]) -> int:
    result = 0
    for i,_ in enumerate(data_matrix):
        for j, char in enumerate(data_matrix[i]):
            if char == '.':
                tmp_matrix = data_matrix.copy()
                tmp_matrix[i] = data_matrix[i][:j] + '#' + data_matrix[i][j+1:]
                if path_length(tmp_matrix) == -1:
                    result += 1

    return  result

# let path_length return the actual path
# and only put blockers on that
def better_way(data_matrix: list[str]) -> int:
    pass

def solve(data: str):
    data_matrix = data.splitlines()

    result = 0
    for i,_ in enumerate(data_matrix):
        for j, char in enumerate(data_matrix[i]):
            if char == '.':
                tmp_matrix = data_matrix.copy()
                tmp_matrix[i] = data_matrix[i][:j] + '#' + data_matrix[i][j+1:]
                if path_length(tmp_matrix) == -1:
                    result += 1

    return  result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")