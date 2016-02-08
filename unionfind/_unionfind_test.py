import pytest
from quickfind import QuickFind
from quickunion import QuickUnion
from weightedquickunion import WeightedQuickUnion
from wqupathcompression import WQUPathCompression

#
# Test for Quick Find data structure
#
def make_qf_10():
	qf = QuickFind(10)	
	qf.union(0, 1)
	qf.union(2, 3)
	qf.union(4, 5)
	qf.union(6, 7)
	qf.union(8, 9)
	return qf	

def test_qf_state():
	qf = make_qf_10()
	assert qf.parent == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]

def test_qf_connected():
	qf = make_qf_10()
	assert qf.connected(0, 1) == True
	assert qf.connected(2, 3) == True
	assert qf.connected(4, 5) == True
	assert qf.connected(6, 7) == True
	
def test_qf_not_connected():	
	qf = make_qf_10()
	assert qf.connected(1, 2) == False
	assert qf.connected(3, 4) == False
	assert qf.connected(5, 6) == False
	assert qf.connected(7, 8) == False

#
# Test for Quick Union data structure
#
def make_qu_10():
	qu = QuickUnion(10)	
	qu.union(0, 1)
	qu.union(2, 3)
	qu.union(4, 5)
	qu.union(6, 7)
	qu.union(8, 9)
	return qu	

def test_qu_state():
	qu = make_qu_10()
	assert qu.parent == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]

def test_qu_connected():
	qu = make_qu_10()
	assert qu.connected(0, 1) == True
	assert qu.connected(2, 3) == True
	assert qu.connected(4, 5) == True
	assert qu.connected(6, 7) == True
	
def test_qu_not_connected():	
	qu = make_qu_10()
	assert qu.connected(1, 2) == False
	assert qu.connected(3, 4) == False
	assert qu.connected(5, 6) == False
	assert qu.connected(7, 8) == False	

#
# Test for Weighted Quick Union data structure
#
def make_wqu_10():
	wqu = WeightedQuickUnion(10)	
	wqu.union(0, 1)
	wqu.union(2, 3)
	wqu.union(4, 5)
	wqu.union(6, 7)
	wqu.union(8, 9)
	return wqu	

def test_wqu_state():
	wqu = make_wqu_10()
	assert wqu.parent == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]

def test_wqu_connected():
	wqu = make_wqu_10()
	assert wqu.connected(0, 1) == True
	assert wqu.connected(2, 3) == True
	assert wqu.connected(4, 5) == True
	assert wqu.connected(6, 7) == True
	
def test_wqu_not_connected():	
	wqu = make_wqu_10()
	assert wqu.connected(1, 2) == False
	assert wqu.connected(3, 4) == False
	assert wqu.connected(5, 6) == False
	assert wqu.connected(7, 8) == False		

#
# Test for Weighted Quick Union with Path Compression data structure
#
def make_wqupc_10():
	wqupc = WQUPathCompression(10)	
	wqupc.union(0, 1)
	wqupc.union(2, 3)
	wqupc.union(4, 5)
	wqupc.union(6, 7)
	wqupc.union(8, 9)
	return wqupc	

def test_wqupc_state():
	wqupc = make_wqupc_10()
	assert wqupc.parent == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]

def test_wqupc_connected():
	wqupc = make_wqupc_10()
	assert wqupc.connected(0, 1) == True
	assert wqupc.connected(2, 3) == True
	assert wqupc.connected(4, 5) == True
	assert wqupc.connected(6, 7) == True
	
def test_wqupc_not_connected():	
	wqupc = make_wqupc_10()
	assert wqupc.connected(1, 2) == False
	assert wqupc.connected(3, 4) == False
	assert wqupc.connected(5, 6) == False
	assert wqupc.connected(7, 8) == False			