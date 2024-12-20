import timeit
import re

test_data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
test_answer = 48

data: str = ''
with open('.\\day_3\\data.txt', 'r') as f:
    data = f.read()

def solve(data: str):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')
    matches = re.finditer(pattern, data)
    enabled = True
    result = 0
    for match in matches:
        if match.group() == 'do()':
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif enabled:
            digits = match.group().removeprefix('mul(').removesuffix(')').split(',')
            result += int(digits[0]) * int(digits[1])
    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")