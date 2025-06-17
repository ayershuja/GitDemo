import pytest

@pytest.fixture(scope="class")
#@pytest.fixture()
def setup():
    print("I will be executed before the test starts")
    yield
    print("I will be executed after the test ends")

@pytest.fixture()
def dataLoad():
    print("user profile data is created")
    return ["Ayer","Shuja","URLData"]

@pytest.fixture(params=["chrome","firefox"])
def crossBrowser(request):
    return request.param