from abcd import bar
from abcd import foo
import pytest
foo1 = None

def test_abcd(mocker):
    foo1 = mocker.patch('abcd.foo')
    foo1.side_effect=mocked_foo
    bar(10)   
    foo1.assert_called

def mocked_foo(val):
    fp = open("foo.dat",'w')
    fp.write("bar")
    fp.close()


