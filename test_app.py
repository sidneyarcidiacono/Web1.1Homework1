################################################################################
## IMPORTANT: DO NOT EDIT THIS CODE.
##
## To run the tests, first make sure you have pytest installed:
##
## $ pip3 install pytest
##
## Then, open up a terminal to the homework folder and run the following:
##
## $ pytest
##
## If you want to run only a single test, you can run the following:
##
## $ pytest -k 'test_penguins'
################################################################################

import pytest

from app import app

def test_index():
    """Test that the index page shows "Are you there, world? It's me, Ducky!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = 'Are you there, world? It\'s me, Ducky!'
    assert expected_page_text == result_page_text

def test_penguins():
    """Test that the /penguins route shows "Penguins are cute!" """
    res = app.test_client().get('/penguins')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = 'Penguins are cute!'
    assert expected_page_text == result_page_text

def test_favorite_animal_donkey():
    """Test that the /animal/ANIMAL route shows an appropriate result."""
    res = app.test_client().get('/animal/donkey')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'donkey' in result_page_text
    assert 'zebra' not in result_page_text

def test_favorite_animal_zebra():
    """Test that the /animal/ANIMAL route shows an appropriate result."""
    res = app.test_client().get('/animal/zebra')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'zebra' in result_page_text
    assert 'donkey' not in result_page_text

def test_favorite_dessert_donuts():
    """Test the /dessert/DESSERT route."""
    res = app.test_client().get('/dessert/donuts')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'donuts' in result_page_text
    assert 'apple pie' not in result_page_text

def test_favorite_dessert_apple_pie():
    """Test the /dessert/DESSERT route."""
    res = app.test_client().get('/dessert/apple%20pie')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'apple pie' in result_page_text
    assert 'donuts' not in result_page_text

def test_madlibs():
    """Test the /madlibs/ADJECTIVE/NOUN route."""
    res = app.test_client().get('/madlibs/purple/banana')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'purple' in result_page_text
    assert 'banana' in result_page_text

def test_multiply_6_7():
    """Test the /multiply/X/Y route."""
    res = app.test_client().get('/multiply/6/7')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = '6 times 7 is 42.'
    assert expected_page_text == result_page_text

def test_multiply_123_456():
    """Test the /multiply/X/Y route."""
    res = app.test_client().get('/multiply/123/456')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = '123 times 456 is 56088.'
    assert expected_page_text == result_page_text

def test_sayntimes_random_5():
    """Test sayntimes/word/number route"""
    res = app.test_client().get('sayntimes/random/5')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = 'random random random random random '
    assert expected_page_text == result_page_text

def test_reverse_random():
    """Test /reverse/word route"""
    res = app.test_client().get('/reverse/random')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = 'modnar'
    assert expected_page_text == result_page_text

def test_strangecaps_hello():
    """Test /strangecaps/word route"""
    res = app.test_client().get('/strangecaps/hello')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = 'HeLlO'
    assert expected_page_text == result_page_text

def test_dicegame():
    res = app.test_client().get('/dicegame')
    assert res.status_code == 200
    
