from time import sleep
import timeit
import pprint

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
test_answer = 12

data: str = ''
with open('.\\day_14\\data.txt', 'r') as f:
    data = f.read()

type Point = tuple[int,int]

# Robot = position, velocity
type Robot = tuple[Point,Point]

# 11,7 for test
width = 11
height = 7

# 101, 103 for run
width = 101
height = 103

# In: p=6,3 v=-1,-3
# Out: (6,3), (-1,-3)
def parse_robot(data: str) -> Robot:
    p = data.split(' v=')[0]
    v = data.split(' v=')[1]
    x, y = p.split(',')[0], p.split(',')[1]
    vx, vy = v.split(',')[0], v.split(',')[1]
    return ((int(x.split('=')[1]), int(y)), (int(vx), int(vy)))

def pprint_robot(robots: list[Robot], fileName=None):
    map: list[list[int]] = [[0 for i in range(width)] for j in range(height)]
    for robot in robots:
        x, y = robot[0]
        map[y][x] = map[y][x] + 1
    map_str = [[str(cell) if cell > 0 else '.' for cell in row] for row in map]

    if not fileName is None:
        with open('.\\day_14\\' + fileName, 'a') as f:
            for row in map_str:
                f.write(''.join(row) + '\n')
            f.write('\n')
    else:
        pprint.pprint(map_str)


def solve(data: str) -> int:
    robots: list[tuple[tuple[int, int], tuple[int, int]]] = [parse_robot(line) for line in data.split('\n')]
    
    for i, robot in enumerate(robots):
        x, y = robot[0]
        vx, vy = robot[1]
        new_x = (x + 100*vx) % width
        new_y = (y + 100*vy) % height
        robot = ((new_x,new_y), (vx,vy))
        robots[i] = robot
    # pprint_robot(robots, 'output.txt')

    qs = [0,0,0,0]
    for robot in robots:
        x, y = robot[0]
        if x < width//2 and y < height//2:
            qs[0] += 1
        if x > width//2 and y < height//2:
            qs[1] += 1
        if x < width//2 and y > height//2:
            qs[2] += 1
        if x > width//2 and y > height//2:
            qs[3] += 1
    #print(f'''q1: {qs[0]}, q2: {qs[1]}, q3: {qs[2]}, q4: {qs[3]}, result: {qs[0]*qs[1]*qs[2]*qs[3]}''')
    return qs[0]*qs[1]*qs[2]*qs[3]

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")