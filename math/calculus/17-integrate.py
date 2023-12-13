#!/usr/bin/env python3

"""calcul of the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
    Function to calculates the integral of a polynomial

    @param poly - list of coefficients representing a polynomial
    @return list of coefficients representing the integral of the polynomial
    """

    if not isinstance(poly, list) or len(poly) < 1:
        return None
    if type(C) is not int and type(C) is not float:
        return None

    if poly == [0]:
        return [C]
    result = all(type(n) in [int, float] for n in poly)
    if not result:
        return None
    poly.insert(0, C)
    for x in range(1, len(poly)):
        poly[x] = poly[x] / x
    for y in range(len(poly)):
        if poly[y] % 1 == 0:
            poly[y] = int(poly[y])
    return poly
