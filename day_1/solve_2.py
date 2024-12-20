import timeit

from solve_1 import read_lists

test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
test_answer = 31

data = ''
with open('.\\day_1\\data.txt', 'r') as f:
    data = f.read()

def solve(data):
    (l1, l2) = read_lists(data)
    # easy but not super efficient
    return sum([l2.count(x) * x for x in l1])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")