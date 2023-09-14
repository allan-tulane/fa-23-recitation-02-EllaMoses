from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(16, 4, 2) == 496
	assert simple_work_calc(1, 4, 3) == 1

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) ==  300
	assert work_calc(8, 2, 2,lambda n: 2) == 22
	assert work_calc(2, 1, 2, lambda n: n*n*n) == 9
	assert work_calc(16, 3, 2, lambda n: n-1) ==  171