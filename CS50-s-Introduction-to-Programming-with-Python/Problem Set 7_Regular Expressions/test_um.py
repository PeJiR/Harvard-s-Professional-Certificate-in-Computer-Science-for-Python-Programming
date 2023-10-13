from um import count

def main():
    test_uppper_lower_case()
    test_word_with_um()
    test_surround_by_um()



def test_uppper_lower_case():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test_word_with_um():
    assert count("Yummi") == 0

def test_surround_by_um():
    assert count("Hello, um world" ) == 1
    assert count ("um? ") == 1

if __name__=="__main__":
    main()











