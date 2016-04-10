#include "QuickFind.h"

QuickFind::QuickFind(int size): UnionFind(size) {

}

void QuickFind::connect(int p, int q) {
	int pId = find(p);
	int qId = find(q);

	if (pId == qId) {
		return;
	}

	for (int i = 0; i < parents.size(); i++) {
		if (parents[i] == pId) {
			parents[i] = qId;
		}
	}
	connectedComponents--;
}

int QuickFind::find(int p) {
	return parents[p];
}