import enum
import timeit

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
test_answer = 480

# x movement, y movement
type Button = tuple[int,int]
type Prize = tuple[int,int]

data: str = ''
with open('.\\day_13\\data.txt', 'r') as f:
    data = f.read()

def parse_button(data: str):
    xy = data.split(': ')[1]
    x, y = xy.split(',')[0], xy.split(',')[1]
    return (int(x.split('+')[1]), int(y.split('+')[1]))

def parse_prize(data: str):
    xy = data.split(': ')[1]
    x, y = xy.split(',')[0], xy.split(',')[1]
    return (int(x.split('=')[1]), int(y.split('=')[1]))

def solve(data: str):
    unparsed_problems = data.split('\n\n')

    result = 0
    for prob in unparsed_problems:

        prob_lines = prob.split('\n')
        buttonA = parse_button(prob_lines[0])
        buttonB = parse_button(prob_lines[1])
        prize = parse_prize(prob_lines[2])

        # find a solution to 
        # minimize 3*a + b
        # prize.x = a * buttonA.x + b * buttonB.x
        # prize.y = a * buttonA.y + b * buttonB.y
        # 0 <= a, b <= 100

        # while a nice ILP, just enumerating works fine...
        # though part 2 will kill this probably
        for i in range(0,101):
            for j in range(0,101):
                if prize[0] == i * buttonA[0] + j * buttonB[0] and prize[1] == i * buttonA[1] + j * buttonB[1] and i <= 100 and j <= 100:
                    result += 3*i+j
    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")