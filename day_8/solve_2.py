import timeit
import pprint

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
test_answer = 34

data: str = ''
with open('.\\day_8\\data.txt', 'r') as f:
    data = f.read()

def prettyprint_grid(data: list[str], antennas, antilocations):
    num_rows = len(data)
    num_cols = len(data[0])
    grid = [['.' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in antennas:
                grid[i][j] = char
            if (i, j) in antilocations and grid[i][j] == '.':
                grid[i][j] = '#'
    grid: list[str] = [''.join(row) for row in grid]
    pprint.pprint(grid)

def solve_any_on_line(data:str):
    lines: list[str] = data.splitlines()
    antennas: dict[str, list[(int,int)]] = {}
    for ix, line in enumerate(lines):
        for jx, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((ix, jx))
    # pprint.pprint(antennas)

    num_rows: int = len(lines)
    num_cols: int = len(lines[0])

    antilocations = set([])

    for antenna in antennas:
        locations = antennas[antenna]
        for i, A in enumerate(locations):
            for j, B in enumerate(locations):
                if i == j:
                    continue
                dist0 = A[0] - B[0]
                dist1 = A[1] - B[1]
    pass

'''
Puzzle example implies to extend antinodes with arbitrary steps
Text implies all cells on the line A-B are antinodes
Below solves the first and returns a to low answer

Below is correct with: the antennas themselves are also antinodes
so they need to be added to the location set
'''
def solve_steps(data: str):
    lines: list[str] = data.splitlines()
    
    antilocations = set([])
    antennas: dict[str, list[(int,int)]] = {}
    for ix, line in enumerate(lines):
        for jx, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((ix, jx))
                antilocations.add((ix, jx))
    # pprint.pprint(antennas)

    num_rows: int = len(lines)
    num_cols: int = len(lines[0])


    for antenna in antennas:
        locations = antennas[antenna]
        for i, A in enumerate(locations):
            for j, B in enumerate(locations):
                if i == j:
                    continue
                dist0 = A[0] - B[0]
                dist1 = A[1] - B[1]

                anti = (A[0]+dist0, A[1]+dist1)
                while 0 <= anti[0] < num_rows and 0 <= anti[1] < num_cols:
                    antilocations.add(anti)
                    anti = (anti[0]+dist0, anti[1]+dist1)
    # prettyprint_grid(lines, antennas, antilocations)
    return len(antilocations) + 0

def solve(data: str):
    return solve_steps(data)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")