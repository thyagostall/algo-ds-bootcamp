CC = g++
CFLAGS = -std=c++11 -Wall -c
LFLAGS = -std=c++11 -Wall
DEBUG = -g
OBJS = main.o QuickFind.o QuickUnion.o UnionFind.o WeightedQuickUnion.o UFPathCompression.o

a.out: $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) $(DEBUG)

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp $(DEBUG)

QuickUnion.o: unionfind/UnionFind.h unionfind/QuickUnion.h unionfind/QuickUnion.cpp
	$(CC) $(CFLAGS) unionfind/QuickUnion.cpp $(DEBUG)

QuickFind.o: unionfind/UnionFind.h unionfind/QuickFind.h unionfind/QuickFind.cpp
	$(CC) $(CFLAGS) unionfind/QuickFind.cpp $(DEBUG)

WeightedQuickUnion.o: unionfind/UnionFind.h unionfind/WeightedQuickUnion.h unionfind/WeightedQuickUnion.cpp
	$(CC) $(CFLAGS) unionfind/WeightedQuickUnion.cpp $(DEBUG)	

UFPathCompression.o: unionfind/UnionFind.h unionfind/UFPathCompression.h unionfind/UFPathCompression.cpp
	$(CC) $(CFLAGS) unionfind/UFPathCompression.cpp $(DEBUG)		

UnionFind.o: unionfind/UnionFind.h unionfind/UnionFind.cpp
	$(CC) $(CFLAGS) unionfind/UnionFind.cpp $(DEBUG)