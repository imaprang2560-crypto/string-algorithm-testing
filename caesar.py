from caesar import caesar_cipher


# lowercase
def test_lowercase():

    assert caesar_cipher("abc",2) == "cde"


# wrap around
def test_wrap():

    assert caesar_cipher("xyz",3) == "abc"


# uppercase
def test_uppercase():

    assert caesar_cipher("ABC",2) == "CDE"


# special character
def test_special():

    assert caesar_cipher("hello!",5) == "mjqqt!"


# mix case
def test_mix():

    assert caesar_cipher("AbC",1) == "BcD"