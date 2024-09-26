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