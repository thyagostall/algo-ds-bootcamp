#include "QuickUnion.h"

QuickUnion::QuickUnion(int size): UnionFind(size) {

}

void QuickUnion::connect(int p, int q) {
	int pRoot = find(p);
	int qRoot = find(q);

	if (pRoot == qRoot) {
		return;
	}

	parents[pRoot] = qRoot;

	connectedComponents--;
}

int QuickUnion::find(int p) {
	while (p != parents[p]) {
		p = parents[p];
	}
	return p;
}