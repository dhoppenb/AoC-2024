import timeit
import re

test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test_answer = 161

data: str = ''
with open('.\\day_3\\data.txt', 'r') as f:
    data = f.read()

def mul(mul_str):
    return int(mul_str[0]) * int(mul_str[1])

def solve(data: str):
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    muls = re.findall(mul_pattern, data)
    return sum(map(mul, muls))

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")