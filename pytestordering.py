import pytest
@pytest.mark.run(order=2)
def test_methodB():
	print('demo:test_methodB execution..')

@pytest.mark.run(order=3)
def test_methodC():
	print('demo:test_methodC execution..')

@pytest.mark.run(order=1)
def test_methodA():
	print('demo:test_methodA execution..')