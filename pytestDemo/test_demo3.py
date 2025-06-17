import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    def test_fixture(self):
        print("I will execute steps in fixuture demonstration")

    def test_fixture2(self):
        print("I will execute steps in fixuture2 demonstration")

    def test_fixture3(self):
        print("I will execute steps in fixuture3 demonstration")

    def test_fixture4(self):
        print("I will execute steps in fixuture4 demonstration")