from hexlet_pytest.stack import stack
from pytest import raises


def test_stack():
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


stack.clear()


def test_emptiness():
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with raises(IndexError):
        stack.pop()
