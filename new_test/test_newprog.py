### test file for newprog.py

import newprog

def test_func():
	variable1 = 1
	variable2 = 0
	import ipdb; ipdb.set_trace()
	assert newprog.func(variable1, variable2) == "True"


