class WQUPathCompression:
	def __init__(self, size):
		self.parent = list(range(size))
		self.sizes = [1] * size

	def union(self, p, q):
		i = self._find(p)
		j = self._find(q)
		if i == j:
			return

		if self.sizes[i] < self.sizes[j]:
			self.parent[i] = self.parent[j]
			self.sizes[j] += self.sizes[i]
		else:
			self.parent[j] = self.parent[i]
			self.sizes[i] += self.sizes[j]

	def _find(self, p):
		root = self.parent[p]
		while root != self.parent[root]:
			root = self.parent[root]

		# Flattens the tree
		i = p
		while i != self.parent[root]:
			temp = i
			i = self.parent[i]
			self.parent[temp] = root
		
		return root

	def connected(self, p, q):
		return self._find(p) == self._find(q)