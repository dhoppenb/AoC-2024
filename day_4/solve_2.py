import timeit

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test_answer = 9

data: str = ''
with open('.\\day_4\\data.txt', 'r') as f:
    data = f.read()

directions = [
    [(-1,-1), (1,1)],
    [(-1,1), (1,-1)],
]

def checkXMAS(location, chardict):
    (i,j) = location
    twoMAS = True
    for direction in directions:
        (ai, aj) = direction[0]
        (bi, bj) = direction[1]
        oneMAS = (chardict.get((i+ai, j+aj), '') == 'M' and chardict.get((i+bi, j+bj), '') == 'S' or 
                  chardict.get((i+ai, j+aj), '') == 'S' and chardict.get((i+bi, j+bj), '') == 'M')
        twoMAS = twoMAS and oneMAS
    return twoMAS

def solve(data: str):
    lines: list[str] = data.splitlines()
    data_matrix: list[list[str]] = [list(line.rstrip()) for line in lines] 

    chardict = {}
    achars = []
    for i, _ in enumerate(data_matrix):
        for j, char in enumerate(data_matrix[i]):
            chardict[(i,j)] = char
            if char == 'A':
                achars.append((i,j))

    return sum([checkXMAS(location, chardict) for location in achars])

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")