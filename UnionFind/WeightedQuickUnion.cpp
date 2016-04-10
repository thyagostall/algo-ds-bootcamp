#include "WeightedQuickUnion.h"

WeightedQuickUnion::WeightedQuickUnion(int size): QuickUnion(size), sizes(size) {
	for (int i = 0; i < size; i++) {
		sizes[i] = 1;
	}
}

void WeightedQuickUnion::connect(int p, int q) {
	int i = find(p);
	int j = find(q);

	if (i == j) {
		return;
	}

	if (sizes[i] < sizes[j]) {
		parents[i] = j;
		sizes[j] += sizes[i];
	} else {
		parents[j] = i;
		sizes[i] += sizes[j];
	}
	connectedComponents--;
}

int WeightedQuickUnion::find(int p) {
	while (p != parents[p]) {
		p = parents[p];
	}
	return p;
}