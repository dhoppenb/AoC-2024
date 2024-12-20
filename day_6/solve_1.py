import timeit
import pprint

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
test_answer = 41

data: str = ''
with open('.\\day_6\\data.txt', 'r') as f:
    data = f.read()

def change_dir(direction: list[int]) -> list[int]:
    rot90cw = [
        [0, 1],
        [-1, 0]
    ]
    return [
        rot90cw[0][0]*direction[0] + rot90cw[0][1]*direction[1],
        rot90cw[1][0]*direction[0] + rot90cw[1][1]*direction[1]
    ]

def path_length(data_matrix: list[str]) -> int:
    num_rows = len(data_matrix)
    num_cols = len(data_matrix[0])

    visited = set([])
    direction = [-1, 0]

    # Find the starting position
    start = (0, 0)
    for i, row in enumerate(data_matrix):
        if '^' in row:
            start = (i, row.index('^'))
            break
    
    loop_count = 0
    while loop_count < 1e4:
        loop_count += 1
        visited.add(start)
        # Check if we can move forward
        forward = (start[0] + direction[0], start[1] + direction[1])
        if 0 <= forward[0] < num_rows and 0 <= forward[1] < num_cols and data_matrix[forward[0]][forward[1]] in ['.','X', '^']:
            start = forward
            # add path for debug
            # data_matrix[forward[0]] = data_matrix[forward[0]][:forward[1]] + 'X' + data_matrix[forward[0]][forward[1]+1:]
        # If not turn right
        elif 0 <= forward[0] < num_rows and 0 <= forward[1] < num_cols and data_matrix[forward[0]][forward[1]] == '#':
            direction = change_dir(direction)
        else:
            break
        # print the path for debug
        # pprint.pprint(data_matrix)

    return len(visited)

def solve(data: str):
    data_matrix = data.splitlines()
    return path_length(data_matrix)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")