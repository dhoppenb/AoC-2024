import timeit

test_data = """1,2,3"""
test_answer = 6

data: str = ''
with open('.\\day_12\\data.txt', 'r') as f:
    data = f.read()

# Similar to part 1 but count corners for a region
# for some f(corners) -> sides?
def solve(data: str):
    pass

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")