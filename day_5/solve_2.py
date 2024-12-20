import timeit
import pprint

from solve_1 import valid_item_list

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
test_answer = 123

data: str = ''
with open('.\\day_5\\data.txt', 'r') as f:
    data = f.read()

def topo_sort(adj_list: dict) -> list[str]:
    visited = set()
    stack = []
    def dfs(node: str):
        visited.add(node)
        if node in adj_list:
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        stack.append(node)
    for node in adj_list:
        if node not in visited:
            dfs(node)
    return stack[::-1]

def solve(data: str):
    split = data.split('\n\n')
    orderings = split[0].splitlines()
    itemlists = split[1].splitlines()

    adj_list = {}
    for ordering in orderings:
        a, b = ordering.split('|')
        if a not in adj_list:
            adj_list[a] = []
        adj_list[a].append(b)

    result = 0
    for itemlist in itemlists:
        if not valid_item_list(itemlist, adj_list):
            items = itemlist.split(',')

            # The full ordering set is cyclic
            # but the reduced list isn't... 
            reduced_adj_list = {}
            for i in items:
                if i in adj_list:
                    reduced_adj_list[i] = adj_list[i]

            toposort = topo_sort(reduced_adj_list)
            ordered = [x for x in toposort if x in items]
            result += int(ordered[len(ordered) // 2])

    return result

def test():
    assert solve(test_data) == test_answer

if __name__ == '__main__':
    print(solve(data))   
    iters = 10 
    t = timeit.timeit('solve(data)', globals=globals(), number=iters)
    print(f" Time: {t*1e3/iters:.2f} ms")