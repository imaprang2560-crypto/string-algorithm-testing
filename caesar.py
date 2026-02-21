from caesar import caesar_cipher

def test_lowercase():

    assert caesar_cipher("abc",2)=="cde"


def test_wrap():

    assert caesar_cipher("xyz",3)=="abc"


def test_uppercase():

    assert caesar_cipher("ABC",2)=="CDE"


def test_special():

    assert caesar_cipher("hello!",5)=="mjqqt!"