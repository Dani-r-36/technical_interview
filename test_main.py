from main import main, random_letter, player_rack

import pytest 

def test_ind_GUAR():
    response = main("G")
    assert response == 2
    response = main("U")
    assert response == 1
    response = main("A")
    assert response == 1
    response = main("R")
    assert response == 1

def test_GUARDIAN():
    response = main("GUARDIAN")
    assert response == 10

def test_seven_titles():
    response = player_rack()
    assert len(response) == 7
    assert isinstance(response,list)