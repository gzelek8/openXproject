import tree
from node import Node

root_for_test = tree.Tree(4)


def test_insert():
    """Check if add value is correct"""
    node = Node(5)
    result = root_for_test.insert(4, node, "left")

    assert type(result) is Node
    assert node.left is result
    assert result.value == 4
    assert result.left is None and result.right is None


# _______________________________________
def test_calculate_sum():
    """Check that sum is correct"""
    node = Node(5)

    result = root_for_test.calculate_sum(node)

    assert result == 5
    assert type(result) is int


def test_calculate_sum_with_none_node():
    """Check if n1 is None"""
    n1 = None

    result = root_for_test.calculate_sum(n1)

    assert result == 0


def test__calculate_sum():
    """Check if sum is correct"""
    n1 = root_for_test.insert(3, root_for_test, "right")
    n2 = root_for_test.insert(4, n1, "left")
    n3 = root_for_test.insert(4, n2, "left")

    root_for_test._calculate_sum(n1)
    result = root_for_test.sum

    assert result == 11
    assert type(result) is int


def test__calculate_sum_with_none_node():
    """Check if sum is correct"""
    n1 = None

    result = root_for_test._calculate_sum(n1)

    assert result is None


# ______________________________________________________________
def test_calculate_average():
    """Check that average is correct"""
    n1 = root_for_test.insert(3, root_for_test, "left")
    n2 = root_for_test.insert(5, n1, "left")

    result = root_for_test.calculate_average(n1)

    assert result == 4


def test_calculate_average_with_none_node():
    """Check if n1 is None"""
    n1 = None

    result = root_for_test.calculate_average(n1)

    assert result == 0


def test__calculate_average():
    """Check if self.average is correct"""
    n1 = root_for_test.insert(3, root_for_test, "right")
    n2 = root_for_test.insert(4, n1, "left")
    n3 = root_for_test.insert(5, n2, "left")

    root_for_test._calculate_average(n1)
    result = root_for_test.average
    assert result == 3


def test__calculate_average_with_none_node():
    """Check if average  is correct when node is none"""
    n1 = None

    result = root_for_test._calculate_average(n1)

    assert result is None


# ____________________________________________________

def test_calculate_median():
    """Check that median is correct"""
    n1 = root_for_test.insert(3, root_for_test, "right")
    n2 = root_for_test.insert(4, n1, "left")
    n3 = root_for_test.insert(5, n2, "left")

    result = root_for_test.calculate_median(n1)
    result2 = root_for_test.calculate_median(n2)
    result3 = root_for_test.calculate_median(n3)

    assert result == 4
    assert result2 == 4.5
    assert result3 == 5


def test_calculate_median_with_none_node():
    """Check if n1 is None"""
    n1 = None

    result = root_for_test.calculate_median(n1)

    assert result is None


def test__calculate_median():
    """Check if self.median is correct and median is ok also"""
    list_of_value = [3, 4, 5]
    n1 = root_for_test.insert(3, root_for_test, "right")
    n2 = root_for_test.insert(4, n1, "left")
    n3 = root_for_test.insert(5, n2, "left")

    root_for_test._calculate_median(n1)
    result = len(root_for_test.median)
    assert result > 0
    assert root_for_test.median == list_of_value


def test__calculate_median_with_none_node():
    """Check if median is correct when node is none"""
    n1 = None

    result = root_for_test._calculate_median(n1)

    assert result is False
