# pylint: disable=redefined-outer-name
import pytest

def test_file1_method1():
    x_var = 5
    y_var = 6
    assert x_var + 1 == y_var, "test method 1-1 failed"
    assert x_var == y_var, "test method 1-2 failed"


def test_file1_method2():
    x_var = 5
    y_var = 6
    assert x_var + 1 == y_var, "test method 2 failed"

def raise_func():
    # raise SystemExit(1)
    raise TypeError("1 is not floating point number")


# Use the raises helper to assert that some code raises an exception
def test_raise():
    with pytest.raises(TypeError):
        raise_func()

class TestClass:
    test = 10
    def test_one(self):
        x_var = "this"
        assert "is" in x_var

    def test_two(self):
        x_var = "hello"
        assert hasattr(x_var, "check")





@pytest.fixture
def supply_a_b():
    src_a = 25
    src_b = 35
    return [src_a, src_b]

def test_compare_a(supply_a_b):
    dst_z = 35
    assert supply_a_b[0] == dst_z, "src_a and dst_z comparison failed"

def test_compare_b(supply_a_b):
    dst_z = 35
    assert supply_a_b[1] == dst_z, "src_b and dst_z comparison failed"


# Parametrizing fixtures
# set to x=0/y=2, x=1/y=2, x=0/y=3, and x=1/y=3
@pytest.mark.parametrize("set_x", [0, 1])
@pytest.mark.parametrize("set_y", [2, 3])
def test_foo(set_x, set_y):
    res = set_x + set_y
    assert res != 3

PARAM_A = 8
PARAM_B = 6
PARAM_C = 6*9
@pytest.mark.parametrize("test_input, expected", [(PARAM_A, 10), (PARAM_B, 6), (PARAM_C, 42)])
def test_val(test_input, expected):
    assert test_input == expected



# Request a unique temporary directory for functional tests

CONTENT = "content"

def test_create_file(tmp_path):
    dir_ = tmp_path / "sub"
    dir_.mkdir()
    target = dir_ / "hello.txt"
    target.write_text(CONTENT)
    assert target.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 2
