import twttr

from twttr import shorten

def main():
    test_upper_lower_cases()
    test_numbers()
    test_puntuation()

def test_upper_lower_cases():
    assert shorten ('twitter') == 'twttr'
    assert shorten ('TWITTER') == 'TWITTR'

def test_numbers():
    assert shorten ('1,2,3,4') == '1,2,3,4'

def test_puntuation():
    assert shorten ('!?.,') == '!?.,'


if __name__ == "__main__":
    main()
