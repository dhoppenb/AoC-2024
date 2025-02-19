import timeit
from scipy.optimize import milp, LinearConstraint, OptimizeResult


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
    return (int(x.split('=')[1])+10000000000000, int(y.split('=')[1])+10000000000000)
#return (int(x.split('=')[1]), int(y.split('=')[1]))

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

        # and it did...
        # let's try a mixed integer linear programming approach
        '''
        c = [3,1]
        A_eq = [[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]]
        b_eq = [prize[0], prize[1]]
        constraints = [LinearConstraint(A_eq, b_eq, b_eq)]
        res: OptimizeResult = milp(c, constraints=constraints, integrality=[1,1])
        if res.success:
            # print(f'Solution: {res.x}, c: {res.fun}')
            result += res.fun'''
        # print(f'total result {result}') # to low anser: 48059778887628
        # maybe numbers are to large 
        # fun to look at an ILP again but unless both buttons are dependent/same direction 
        # there is just a single solution

        # Take prize.x = a * buttonA.x + b * buttonB.x and express a in terms of b
        # substitute that into prize.y = a * buttonA.y + b * buttonB.y
        # and simplify as b = ...
        numerator = (prize[1]*buttonA[0] - prize[0]*buttonA[1])
        denominator = (-1*buttonB[0]*buttonA[1] + buttonB[1]*buttonA[0])
        has_solution_for_b = numerator % denominator == 0
        if has_solution_for_b:
            # if solution exists calc b
            b = numerator // denominator
            # and calc a
            has_solution_for_a = (prize[0] - b*buttonB[0]) % buttonA[0] == 0
            if has_solution_for_a:
                a = (prize[0] - b*buttonB[0]) // buttonA[0]
                result += 3*a+b
     
    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")