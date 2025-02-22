import timeit
from enum import Enum
import pprint

test_data = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
test_answer = 2028

test_data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
test_answer = 10092

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4  

def char2dir(char: str) -> Direction:
    if char == '^':
        return Direction.UP
    elif char == 'v':
        return Direction.DOWN
    elif char == '<':
        return Direction.LEFT
    elif char == '>':
        return Direction.RIGHT
    
def dir2vec(direction: Direction) -> tuple[int,int]:
    if direction == Direction.UP:
        return (0, -1)
    elif direction == Direction.DOWN:
        return (0, 1)
    elif direction == Direction.LEFT:
        return (-1, 0)
    elif direction == Direction.RIGHT:
        return (1, 0)

def pprint_map(map: dict[tuple[int,int],str], fileName=None):
    width = max(map.keys(), key=lambda x: x[0])[0] + 1
    height = max(map.keys(), key=lambda x: x[1])[1] + 1
    result = ""
    for y in range(height):
        for x in range(width):
            result = result + map[(x,y)]
        result = result + '\n'
    if not fileName is None:
        with open('.\\day_15\\' + fileName, 'a') as f:
            f.write(result)
    else:
        print(result)

data: str = ''
with open('.\\day_15\\data.txt', 'r') as f:
    data = f.read()

def parse(data: str) :
    map_str = data.split('\n\n')[0]
    direction_str = data.split('\n\n')[1]

    start = (-1,-1)

    map = {}
    for y, row in enumerate(map_str.split('\n')):
        height = y
        for x, cell in enumerate(row):
            width = x
            map[(x,y)] = cell
            if cell == '@':
                start = (x,y)
    # larger test and run input has directions on multiple lines...
    direction_str = direction_str.replace('\n','')
    directions = [char2dir(char) for char in direction_str]
    return map, start, directions

def score(map)-> int:
    score = 0
    for key in map.keys():
        if map[key] == 'O':
            score += 100*key[1]+key[0]
    return score

def solve(data: str):
    map, robot_location, directions = parse(data)

    for direction in directions:
        # pprint_map(map, 'output.txt')
        vec = dir2vec(direction)

        # cases
        # free space to move
        if map[ (robot_location[0] + vec[0],robot_location[1] + vec[1]) ] == '.':
            map[robot_location] = '.'
            robot_location = (robot_location[0] + vec[0], robot_location[1] + vec[1])
            map[robot_location] = '@'

        # wall
        elif map[(robot_location[0] + vec[0],robot_location[1] + vec[1])] == '#':
            continue

        # box
        else:
            # figure out if there is free space somewhere behind the box and where
            box_location = (robot_location[0] + vec[0], robot_location[1] + vec[1])
            while map[box_location] == 'O':
                box_location = (box_location[0] + vec[0], box_location[1] + vec[1])
            # first cell behind box(es) is a wall
            if map[box_location] == '#':
                continue
            # first cell behind box(es) is free
            if map[box_location] == '.':
                # update current and future robot location cells
                map[robot_location] = '.'
                next_location = (robot_location[0] + vec[0], robot_location[1] + vec[1])
                map[next_location] = '@'
                # move all boxes 
                while next_location != box_location:                    
                    next_location = (next_location[0] + vec[0], next_location[1] + vec[1])
                    map[next_location] = 'O'
                # update to new robot location
                robot_location = (robot_location[0] + vec[0], robot_location[1] + vec[1])

    return score(map)

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")