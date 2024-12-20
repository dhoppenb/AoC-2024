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
test_answer = 14

data: str = ''
with open('.\\day_8\\data.txt', 'r') as f:
    data = f.read()

def solve(data: str):
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

                anti = (A[0]+dist0, A[1]+dist1)
                if 0 <= anti[0] < num_rows and 0 <= anti[1] < num_cols:
                    antilocations.add(anti)
    return len(antilocations)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")