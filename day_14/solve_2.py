import timeit
import pprint
import numpy as np

test_data = """1,2,3"""
test_answer = 6

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

def entropy(robots: list[Robot]) -> int:
    as_nparray = np.array([robot[0] for robot in robots], dtype=np.dtype('int32','int32'))
    hist = np.histogramdd(as_nparray, bins=[10, 10])[0]
    hist /= hist.sum()
    hist = hist.flatten()
    hist = hist[hist.nonzero()]
    entropy = -0.5*np.sum(hist * np.log2(hist))
    return entropy
#return np.sum(hist[0] > 0)

# In: p=6,3 v=-1,-3
# Out: (6,3), (-1,-3)
def parse_robot(data: str) -> Robot:
    p = data.split(' v=')[0]
    v = data.split(' v=')[1]
    x, y = p.split(',')[0], p.split(',')[1]
    vx, vy = v.split(',')[0], v.split(',')[1]
    return ((int(x.split('=')[1]), int(y)), (int(vx), int(vy)))

def pprint_robot(robots: list[Robot], fileName=None, i=0, entropy: float=0):
    map: list[list[int]] = [[0 for i in range(width)] for j in range(height)]
    for robot in robots:
        x, y = robot[0]
        map[y][x] = map[y][x] + 1
    map_str = [[str(cell) if cell > 0 else '.' for cell in row] for row in map]
    
    if not fileName is None and entropy < 2.6:
        with open('.\\day_14\\' + fileName, 'a') as f:
            f.write(f'I: {i}, entropy={entropy}\n')
            for row in map_str:
                f.write(''.join(row) + '\n')
            f.write('\n')
    elif fileName is None:
        pprint.pprint(map_str)

# Calculate each iteration
# calculate entropy of current state
# print to file if below threshold (eyeballed to 3)
# for automation entropy<2.6 seems to be the right threshold :)
def solve(data: str):
    robots: list[tuple[tuple[int, int], tuple[int, int]]] = [parse_robot(line) for line in data.split('\n')]

    for i in range(10000):
        entropy_value = entropy(robots)
        pprint_robot(robots, 'output.txt', i, entropy=entropy_value)
        # step
        for i, robot in enumerate(robots):
            x, y = robot[0]
            vx, vy = robot[1]
            x += vx
            y += vy
            x = x % width
            y = y % height
            robot = ((x,y), (vx,vy))
            robots[i] = robot
    return 0

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    #iters = 10 
    #t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    #print(f" Time: {t*1e3/iters:.2f} ms")