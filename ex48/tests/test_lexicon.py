from nose2.tools import *
from ex48 import lexicon

def test_directions():
    assert lexicon.scan('North') == [('direction', 'north')]
    result = lexicon.scan('north SOUTH east')

    assert result == [('direction', 'north'),
                      ('direction', 'south'),
                      ('direction', 'east')]

def test_verbs():
    assert lexicon.scan('open') == [('verb', 'open')]
    result = lexicon.scan('open go fight')

    assert result == [('verb', 'open'),
                     ('verb', 'go'),
                     ('verb', 'fight')]

def test_stops():
    assert lexicon.scan('the') == [('stops', 'the')]
    result = lexicon.scan('the from at')

    assert result == [('stops', 'the'),
                     ('stops', 'from'),
                     ('stops', 'at')]

def test_nouns():
    assert lexicon.scan('bear') == [('noun', 'bear')]
    result = lexicon.scan('bear door princess')

    assert result == [('noun', 'bear'),
                     ('noun', 'door'),
                     ('noun', 'princess')]

def test_numbers():
    assert lexicon.scan('1234') == [('num', 1234)]
    result = lexicon.scan('3 91234')

    assert result == [('num', 3),
                     ('num', 91234)]

def test_errors():
    assert lexicon.scan('sadfefsafergsag') == [('error', 'sadfefsafergsag')]
    result = lexicon.scan('open sadfefsafergsag bear')

    assert result == [('verb', 'open'),
                     ('error', 'sadfefsafergsag'),
                     ('noun', 'bear')]
