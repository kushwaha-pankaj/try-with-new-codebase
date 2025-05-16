Title: Minimum Cost to Connect All Nodes

```python
class Solution:
    def minCostToConnectNodes(self, n: int, edges: List[List[int]], newEdges: List[List[int]]) -> int:
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        existingEdgesCount = 0
        for u, v in edges:
            if union(u, v):
                existingEdgesCount += 1

        if existingEdgesCount == n - 1:
            return 0

        newEdges.sort(key=lambda x: x[2])
        cost = 0
        for u, v, weight in newEdges:
            if union(u, v):
                cost += weight
                existingEdgesCount += 1
                if existingEdgesCount == n - 1:
                    return cost

        return -1
```