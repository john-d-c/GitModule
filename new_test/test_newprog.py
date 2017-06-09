### test file for newprog.py

import newprog

#def test_func():
#	variable1 = 1	variable2 = 0
#	import ipdb; ipdb.set_trace()
#	assert newprog.func(variable1, variable2) == "True"

def test_func_():
    assert newprog.func(1, 2) == "False"
    assert newprog.func(1, 1) == "True"
