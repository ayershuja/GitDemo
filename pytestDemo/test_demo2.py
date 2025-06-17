import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    message = "Hello World"
    assert message == "Hi" ,"Test Failed beacuse message is not equal to Hello World"


def test_SecondCreditCard():
    a=2
    b=3
    assert a+b == 5 ,"Test Pass because a+b is  equal to 5"

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