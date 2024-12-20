import timeit
import pprint

from solve_1 import find_sequence

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
test_answer = 11387

data: str = ''
with open('.\\day_7\\data.txt', 'r') as f:
    data = f.read()

def concat(a, b):
    mul, q = 10, 10
    while q != 0:
        q = b // mul
        if q > 0:
            mul *= 10
    return a * mul + b

# ~5.3s solve duration, not great
def solve(data: str):
    lines = data.splitlines()
    lhs = [int(row.split(':')[0]) for row in lines]
    rhs = [list(map(int, row.split(':')[1].split())) for row in lines]
    operators = [lambda a, b: a+b, 
                 lambda a, b: a*b,
                 concat]
    result = 0
    for i, target in enumerate(lhs):
        if find_sequence(target, rhs[i], operators, 0):
            result += target
    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")