CC = g++
CFLAGS = -std=c++11 -Wall -c
LFLAGS = -std=c++11 -Wall
DEBUG = -g
OBJS = main.o unionfind/UnionFind.o unionfind/QuickUnion.o

a.out: $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) $(DEBUG)

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp $(DEBUG)

unionfind/QuickUnion.o: unionfind/UnionFind.h unionfind/QuickUnion.h unionfind/QuickUnion.cpp
	$(CC) $(CFLAGS) unionfind/QuickUnion.cpp $(DEBUG)

unionfind/UnionFind.o: unionfind/UnionFind.h unionfind/UnionFind.cpp
	$(CC) $(CFLAGS) unionfind/UnionFind.cpp $(DEBUG)