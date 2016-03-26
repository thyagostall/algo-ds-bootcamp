#ifndef UNIONFIND_H
#define UNIONFIND_H

#include <vector>

class UnionFind {
protected:
	int connectedComponents;
	std::vector<int> parents;
public:
	UnionFind(int);

	virtual void connect(int, int) = 0;
	virtual int find(int) = 0;
	bool connected(int, int);
	int count();
};

#endif