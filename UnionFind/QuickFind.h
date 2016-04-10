#ifndef QUICKFIND_H
#define QUICKFIND_H

#include "UnionFind.h"

class QuickFind: public UnionFind {
public:
	QuickFind(int);

	virtual void connect(int, int) override;
	virtual int find(int) override;
};

#endif