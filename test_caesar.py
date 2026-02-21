from caesar import caesar_cipher

def test1():

    assert caesar_cipher("abc",2) == "cde"

def test2():

    assert caesar_cipher("ABC",2) == "CDE"

def test3():

    assert caesar_cipher("xyz",3) == "abc"

def test4():

    assert caesar_cipher("hello!",5) == "mjqqt!"