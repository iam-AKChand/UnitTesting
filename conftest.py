import pytest

@pytest.yield_fixture(scope='module')
def setUpTearDownClass():
	print('setUpClass activity')
	yield
	print('tearDownClass activity')

@pytest.yield_fixture()
def setUpTearDown():
	print('setUp activity')
	yield
	print('tearDown activity')
