import timeit

test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
test_answer = 36

data: str = ''
with open('.\\day_10\\data.txt', 'r') as f:
    data = f.read()

# validate if a direction can be taken
def check_valid_move(int_map: list[list[int]], i, j, prev) -> bool:
    if i < 0 or i >= len(int_map) or j < 0 or j >= len(int_map[0]):
        return False
    return int_map[i][j] == prev+1

# BFS expand from a (0) location to find all 9s
def trailscore_bfs(int_map: list[list[int]], i, j) -> int:
    queue = [(i,j)]
    nines = set() 
    prev = -1
    while queue:
        # print(f'q {queue}')
        i, j = queue.pop(0)
        curr_value = int_map[i][j]
        # out of bounds
        if i < 0 or i >= len(int_map) or j < 0 or j >= len(int_map[0]):
            print(f'out of bounds {i} {j} {prev} {int_map[i][j]}')
            continue
        # reached a 9
        if curr_value == 9:
            nines.add((i,j))
        else:
            if check_valid_move(int_map, i-1, j, curr_value):
                queue.append((i-1,j))
            if check_valid_move(int_map, i+1, j, curr_value):
                queue.append((i+1,j))
            if check_valid_move(int_map, i, j-1, curr_value):
                queue.append((i,j-1))
            if check_valid_move(int_map, i, j+1, curr_value):
                queue.append((i,j+1))
    return len(nines)

def solve(data: str):
    map: list[str] = data.split('\n')
    int_map: list[list[int]] = [[int(c) for c in row] for row in map]

    trailheads = []
    for i, row in enumerate(int_map):
        for j, c in enumerate(row):
            if c == 0:
                trailheads.append((i,j))

    result = sum([trailscore_bfs(int_map, *t) for t in trailheads])

    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")