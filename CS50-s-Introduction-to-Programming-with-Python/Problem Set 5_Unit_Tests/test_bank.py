from bank import value

def main():
    test_return_zero
    test_return_20

def test_return_zero():
    assert value ('hello gi') == 0
    assert value  ('Hello') == 0
    assert value ('HeLlo Gi') == 0


def test_return_20():
    assert value('Hi') == 20
    assert value('hey') == 20


def test_return_100():
    assert value ('What is up')== 100
    assert value ('Good morning') == 100



if __name__ == "__main__":
    main()
