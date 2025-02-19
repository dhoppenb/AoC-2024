import timeit
import pprint

test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
test_answer = 1206

data: str = ''
with open('.\\day_12\\data.txt', 'r') as f:
    data = f.read()

type Point = tuple[int,int]

# Similar to part 1 but count corners for a region
# for some f(corners) -> sides?
def solve(data: str):

    #reuse part 1 for replacing Char with region ID
    map: list[list[str]] = [list(row) for row in data.split('\n')]

    # a global set of visited points
    visited = set[Point]()

    # a dictionary of regions
    # replace the Char with region ID as they are not unique in input
    regions: dict[int, list[Point]] = {}
    id = 0

    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if not visited.__contains__((i,j)):

                visited.add((i,j))
                regions[id] = [(i,j)]
                region_char = map[i][j]

                # BFS from this point to find all connected points
                q = [(i,j)]
                while len(q) > 0:
                    x, y = q.pop()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x+dx, y+dy
                        if nx >= 0 and nx < len(map) and ny >= 0 and ny < len(map[0]) and not visited.__contains__((nx,ny)) and map[nx][ny] == region_char:
                            visited.add((nx,ny))
                            regions[id].append((nx,ny))
                            q.append((nx,ny))
                id += 1

    total_cost = 0
    for key in regions.keys():
        points = regions[key]
        corners = 0
        # check all cases for corners
        for x, y in points:
            # exterior corners
            if (x - 1, y) not in points and (x, y + 1) not in points:
                corners += 1
            if (x - 1, y) not in points and (x, y - 1) not in points:
                corners += 1
            if (x + 1, y) not in points and (x, y + 1) not in points:
                corners += 1
            if (x + 1, y) not in points and (x, y - 1) not in points:
                corners += 1
            # interior corners
            if (x - 1, y) in points and (x, y + 1) in points and (x - 1, y + 1) not in points:
                corners += 1
            if (x - 1, y) in points and (x, y - 1) in points and (x - 1, y - 1) not in points:
                corners += 1
            if (x + 1, y) in points and (x, y + 1) in points and (x + 1, y + 1) not in points:
                corners += 1
            if (x + 1, y) in points and (x, y - 1) in points and (x + 1, y - 1) not in points:
                corners += 1
        # print(f"Region {key} has {corners} corners and {len(points)} points = \t\t{corners*len(points)} cost")
        total_cost += corners * len(points)
                
    return total_cost

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")