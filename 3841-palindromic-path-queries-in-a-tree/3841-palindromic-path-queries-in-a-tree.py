
from typing import List

class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:

        # 1. Build the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n

        # Base prefix XOR masks (before any updates)
        base[0] = 1 << (ord(s[0]) - ord('a'))
        timer = 0

        # 2. Iterative DFS / Euler Tour
        # state 0 = enter node, state 1 = exit node
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v == p:
                        continue

                    depth[v] = depth[u] + 1
                    base[v] = base[u] ^ (
                        1 << (ord(s[v]) - ord('a'))
                    )
                    stack.append((v, u, 0))

            else:
                tout[u] = timer - 1

        # 3. Binary lifting table for LCA
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        # 4. Fenwick Tree supporting range XOR updates
        class Fenwick:
            def __init__(self, size):
                self.tree = [0] * (size + 1)

            def update(self, i, val):
                while i < len(self.tree):
                    self.tree[i] ^= val
                    i += i & -i

            def query(self, i):
                result = 0
                while i > 0:
                    result ^= self.tree[i]
                    i -= i & -i
                return result

        bit = Fenwick(n + 1)
        chars = list(s)
        answer = []

        # 5. Process operations
        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                chars[u] = c

                # Update all root-prefix masks in u's subtree
                bit.update(tin[u] + 1, delta)
                bit.update(tout[u] + 2, delta)

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                # Current root-prefix masks
                mask_u = base[u] ^ bit.query(tin[u] + 1)
                mask_v = base[v] ^ bit.query(tin[v] + 1)

                # XOR mask of characters on the u-v path
                mask = (
                    mask_u
                    ^ mask_v
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                # At most one character may have odd frequency
                answer.append((mask & (mask - 1)) == 0)

        return answer
