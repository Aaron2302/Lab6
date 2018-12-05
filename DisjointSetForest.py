class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):  # <--- find with path compression
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        self.dsf[a] = self.find(self.dsf[a])
        return self.dsf[a]

    def union(self, a, b):  # <--- union by height
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:  # Don't do anything if they belong to the same set already
            return

        if self.dsf[ra] == self.dsf[rb]:  # Trees have the same height
            self.dsf[ra] -= 1
            self.dsf[rb] = ra
        elif self.dsf[ra] < self.dsf[rb]:
            self.dsf[rb] = ra
        else:
            self.dsf[ra] = rb
