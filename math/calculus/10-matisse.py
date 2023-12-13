#!/usr/bin/env python3

"""calcul of the derivative of a polynomial"""


def poly_derivative(poly):
    """
    Function to calculates the derivative of a polynomial

    @param poly - list of coefficients representing a polynomial
    @return list of coefficients representing the derivative of the polynomial
    """

    if not isinstance(poly, list) or len(poly) < 1:
        return None

    if len(poly) == 1:
        return [0]
    for x in range(1, len(poly)):
        poly[x] = poly[x] * x
    poly.pop(0)
    return poly
