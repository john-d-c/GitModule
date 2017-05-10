### test file for newprog.py

import newprog

def test_func():
	import ipdb; ipdb.set_trace()
	variable1 = 1
	variable2 = 0
	import ipdb; ipdb.set_trace()
	assert newprog.func(variable1, variable2) == "True"
