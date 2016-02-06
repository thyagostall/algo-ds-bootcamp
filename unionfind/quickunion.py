class QuickUnion:
	def __init__(self, size):
		self.parent = list(range(size))

	def union(self, p, q):
		self.parent[q] = self.parent[p]

	def _find(self, p):
		parent = self.parent[p]
		while parent != self.parent[parent]:
			parent = self.parent[parent]
		return parent

	def connected(self, p, q):
		return self._find(p) == self._find(q)