from plates import is_valid

def main():
    test_min2_max6()
    test_start2vowals()
    test_number0()
    test_puntuation()
    test_numbermiddle()


def test_min2_max6():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF')== True
    assert is_valid('A') == False
    assert is_valid('ABCDEFG') == False

def test_start2vowals():
    assert is_valid('BB') == True
    assert is_valid ('2A') == False
    assert is_valid("23") == False


def test_number0():
    assert is_valid ('00') == False
    assert is_valid ('01') == False
    assert is_valid ('0') == False
    assert is_valid ('cs50') == True
    assert is_valid ('cs05') == False

def test_puntuation():
    assert is_valid ('PI3.14') == False


def test_numbermiddle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA2AA') == False


if __name__ == "__main__":
    main()
