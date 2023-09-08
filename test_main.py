from main import *

def test_simple_work():
	""" done. """
	'''ask if this test should be work_calc or simple'''
	'''
	assert work_calc(10, 2, 2) == #TODO
	assert work_calc(20, 3, 2) == #TODO
	assert work_calc(30, 4, 2) == #TODO
	'''
	
	assert simple_work_calc(10, 2, 2) == 56
	assert simple_work_calc(20, 3, 2) == 506.75
	assert simple_work_calc(30, 4, 2) == 1954
	assert simple_work_calc(1, 2, 2) == 1
	assert simple_work_calc(2, 2, 2) == 4
	assert simple_work_calc(8, 4, 2) == 120

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 31
	assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
	assert work_calc(30, 3, 2, lambda n: n) ==  638.625
	assert work_calc(8, 2, 2,lambda n: 2) == 22
	assert work_calc(2, 1, 2, lambda n: n*n*n) == 9
	assert work_calc(16, 3, 2, lambda n: n-1) ==  171
