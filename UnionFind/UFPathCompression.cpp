#include "UFPathCompression.h"

UFPathCompression::UFPathCompression(int size): QuickUnion(size), sizes(size) {
	for (int i = 0; i < size; i++) {
		sizes[i] = 1;
	}
}

void UFPathCompression::connect(int p, int q) {
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

int UFPathCompression::find(int p) {
	return root(p);
}

int UFPathCompression::root(int p) {
	int t = p;
	while (t != parents[t]) {
		t = parents[t];
	}

	t = p;
	while (t != parents[t]) {
		t = parents[t];
		parents[t] = p;
	}	
	return p;
}