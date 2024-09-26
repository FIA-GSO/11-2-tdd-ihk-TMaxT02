import pytest
from Ihk import *

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