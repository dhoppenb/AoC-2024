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
test_answer = 1930

data: str = ''
with open('.\\day_12\\data.txt', 'r') as f:
    data = f.read()

type Point = tuple[int,int]

def solve(data: str):
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

    # pprint.pprint(regions)
    result = 0
    # for each region
    for key in regions.keys():
        # determine area
        area = len(regions[key])
        # determine perimeter
        perimeter = 0
        # for each point in the region
        for x, y in regions[key]:
            # for each neighbour
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                # add a perimeter length if neighbour is out of map or part of different region
                if nx < 0 or nx >= len(map) or ny < 0 or ny >= len(map[0]) or map[nx][ny] != map[x][y]:
                    perimeter += 1
        # print(f"Region {key} has area {area} and perimeter {perimeter}")
        result += area * perimeter

    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")