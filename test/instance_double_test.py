from pytest import raises

from doubles import allow, InstanceDouble
from doubles.exceptions import VerifyingDoubleError


class TestInstanceDouble(object):
    def test_allows_stubs_on_existing_methods(self):
        date = InstanceDouble('datetime.date')

        allow(date).to_call('ctime')

        assert date.ctime() is None

    def test_raises_when_stubbing_nonexistent_methods(self):
        date = InstanceDouble('datetime.date')

        with raises(VerifyingDoubleError):
            allow(date).to_call('non_existent_method')

    def test_raises_when_stubbing_noncallable_attributes(self):
        date = InstanceDouble('datetime.date')

        with raises(VerifyingDoubleError):
            allow(date).to_call('year')

    def test_raises_when_argspec_does_not_match(self):
        date = InstanceDouble('datetime.date')

        with raises(VerifyingDoubleError):
            allow(date).to_call('ctime').with_args('foo')

    def test_allows_stubs_on_existing_class_methods(self):
        date = InstanceDouble('datetime.date')

        allow(date).to_call('today')

        assert date.today() is None
