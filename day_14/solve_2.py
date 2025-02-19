import timeit

test_data = """1,2,3"""
test_answer = 6

data: str = ''
with open('.\\day_14\\data.txt', 'r') as f:
    data = f.read()

def solve(data: str):
    pass

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")