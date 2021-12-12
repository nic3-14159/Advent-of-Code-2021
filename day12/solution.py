import sys
from collections import defaultdict
data = [[i.strip() for i in line.split("-")] for line in sys.stdin]
paths = defaultdict(lambda: set())
uniq_paths = set()
for a, b in data:
    paths[a].add(b)
    paths[b].add(a)


def dfs(seen, node):
    count = 0
    if node == "end":
        return 1
    if node in seen:
        return 0
    if node.islower():
        seen.add(node)
    for n in paths[node]:
        count += dfs(seen.copy(), n)
    return count


def dfs2(seen, node, twice, path):
    path.append(node)
    if node == "end":
        uniq_paths.add(",".join(path))
        return 1
    if node in seen:
        return 0
    if node.islower():
        seen.add(node)
    for n in paths[node]:
        dfs2(seen.copy(), n, twice, path.copy())
        if not twice and node != "start" and node.islower():
            seen2 = seen.copy()
            seen2.remove(node)
            dfs2(seen2.copy(), n, True, path.copy())
    return


if __name__ == "__main__":
    print(dfs(set(), "start"))
    dfs2(set(), "start", False, list())
    print(len(uniq_paths))
