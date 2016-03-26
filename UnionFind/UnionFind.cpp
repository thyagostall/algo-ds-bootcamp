#include "UnionFind.h"

UnionFind::UnionFind(int size): parents(size) {
	connectedComponents = size;
	for (int i = 0; i < size; i++) {
		parents[i] = i;
	}
}

bool UnionFind::connected(int p, int q) {
	return find(p) == find(q);
}

int UnionFind::count() {
	return connectedComponents;
}
