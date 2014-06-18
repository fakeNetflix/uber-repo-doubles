from pytest import raises

from doubles import Double, expect, lifecycle
from doubles.proxy import MockExpectationError


class TestExpect(object):
    def test_raises_if_an_expected_method_call_is_not_verified(self):
        subject = Double()

        expect(subject).to_receive('foo')

        with raises(MockExpectationError):
            lifecycle.verify()