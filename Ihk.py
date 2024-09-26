import pytest

def bewerte(prozent):
    if not isinstance(prozent, int):
        raise TypeError("Prozentwert muss eine Zahl")
    if prozent < 0 or prozent > 100:
        raise ValueError("Prozentwert muss zwischen 0 und 100")

    if prozent in range(92, 101):
        return 'sehr gut'
    elif prozent in range(81, 92):
        return 'gut'
    elif prozent in range(67, 81):
        return 'befriedigend'
    elif prozent in range(50, 67):
        return 'ausreichend'
    elif prozent in range(30, 50):
        return 'mangelhaft'
    else:
        return 'ungenügend'

testdaten = [
    (100, 'sehr gut'),
    (92, 'sehr gut'),
    (91, 'gut'),
    (81, 'gut'),
    (80, 'befriedigend'),
    (67, 'befriedigend'),
    (66, 'ausreichend'),
    (50, 'ausreichend'),
    (49, 'mangelhaft'),
    (30, 'mangelhaft'),
    (29, 'ungenügend'),
    (0, 'ungenügend'),
]

throwData = [
    (-1, ValueError),
    (101, ValueError),
    ('text', TypeError)
]

@pytest.mark.parametrize("prozent, erwartet", testdaten)
def test_bewerte(prozent, erwartet):
    assert bewerte(prozent) == erwartet

@pytest.mark.parametrize("prozent, erwartet", throwData)
def test_bewerte_Throw(prozent, erwartet):
    with pytest.raises(erwartet):
        bewerte(prozent)