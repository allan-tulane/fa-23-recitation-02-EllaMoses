"""
CMPS 2200  Recitation 2
"""
### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	""" Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	"""
	The textbook example used floors and ceilings and said that 
	we can normally ignore those since it changes the input size 
	by at most one, so i used integer divison
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1
	else: 
		return a*(simple_work_calc(n//b, a, b)) + n
	
    

def work_calc(n, a, b, f):
	"""
    Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	"""
	The textbook example used floors and ceilings and said that 
	we can normally ignore those since it changes the input size 
	by at most one, so i used integer divison
	"""
	if n ==0:
		return 0
	if n == 1:
		return 1
	else: 
		return a* (work_calc(n//b, a, b, f)) + f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of S(n).
	"""
	if n ==0:
		return 0
	if n == 1:
		return 1
	else: 
		return (span_calc(n//b, a, b, f)) + f(n)
	



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, work_calc(n, 4, 2, work_fn1), work_calc(n, 4, 2, work_fn2)))
	return result





def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work(work_fn1, work_fn2):
	res = compare_work(work_fn1, work_fn2)
	print_results(res)

test_compare_work(lambda n:1, lambda n:n)
test_compare_work(lambda n:n, lambda n: math.log(n))
test_compare_work(lambda n: n ** 2, lambda n: n ** 1.5)
test_compare_work(lambda n: n ** 0.5, lambda n: n ** 3.5)

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append(( n, span_calc(n, 2, 2, span_fn1), span_calc(n,2,2,span_fn2)))
	return result
	

def test_compare_span(span_fn1, span_fn2):
	#span_fn1 = lambda n: 1
	#span_fn2 = lambda n: n
	res = compare_span(span_fn1, span_fn2)
	print_results(res)

test_compare_span(lambda n:1, lambda n:n)
test_compare_span(lambda n:n, lambda n: math.log(n))


