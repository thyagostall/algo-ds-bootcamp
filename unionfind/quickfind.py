class QuickFind:
	def __init__(self, size):
		self.parent = list(range(size))

	def union(self, p, q):
		for i, item in enumerate(self.parent):
			if item == self.parent[q]:
				self.parent[i] = self.parent[p]
		

	def _find(self, p):
		return self.parent[p]

	def connected(self, p, q):
		return self._find(p) == self._find(q)