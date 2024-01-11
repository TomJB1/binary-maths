from binary_maths import *

def test_binary():
    assert binaryNum(5).binary() == "0101"
    assert binaryNum(4).binary() == "0100"
    assert binaryNum(3).binary() == "011"

def test_binary_int():
    assert int(binaryNum(5)) == 5

def test_binary_str():
    assert str(binaryNum(5)) == "0101"


def test_binary_big():
    assert binaryNum(19739832).binary() == "01001011010011010010111000"

def test_binary_negative():
    assert binaryNum(-4).binary() == "100"
    assert binaryNum(-13).binary() == "10011"

def test_binary_big_negative():
    assert binaryNum(-1093024032).binary() == "10111110110110011100011011100000"

def test_binary_add():
    assert int(binaryNum(1)+binaryNum(2)) == 3

def test_binary_minus():
    assert int(binaryNum(1)-binaryNum(2)) == -1