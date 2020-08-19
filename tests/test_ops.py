from sample import ops


def test_add():
    assert ops.add(1, 2) == 3
    assert ops.add(1, -2) == -1


def test_sub():
    assert ops.subtract(1, 2) == -1
    assert ops.subtract(1, -2) == 3


def test_is_valid_yaml():
    assert ops.is_valid_yaml('"') is False
    assert ops.is_valid_yaml('"f"') is True
