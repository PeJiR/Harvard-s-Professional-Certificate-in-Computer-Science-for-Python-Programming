from calculator import square

def main():
    test_square()


class AssetionError:
    pass

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssetionError:
        print("3 square was not 9")


if __name__ == "__main__":
    main()
