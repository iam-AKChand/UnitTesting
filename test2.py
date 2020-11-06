# import pytest

# @pytest.yield_fixture(scope='module')
# def setUpTearDownClass():
# 	print('setUpClass activity')
# 	yield
# 	print('tearDownClass activity')

# @pytest.yield_fixture()
# def setUpTearDown():
# 	print('setUp activity')
# 	yield
# 	print('tearDown activity')


def test_methodB(setUpTearDown,setUpTearDownClass):
	print('demo1:test_methodB execution..')


def test_methodA(setUpTearDown,setUpTearDownClass):
	print('demo1:test_methodA execution..')