#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

El dorește să adauge o unealtă care să permită umplerea unei
forme închise.

Exemplu:

Pornim de la imaginea inițială reprezentată mai jos, trebuie să
umplem formele în care se află "x":

  |-----*------|          |******------|         |************|
  |--x--*------|          |******------|         |************|
  |******------|  ----->  |******------|  -----> |************|
  |-----******-|          |-----******-|         |-----*******|
  |-----*---*--|          |-----*---*--|         |-----*---***|
  |-----*---*-x|          |-----*---*--|         |-----*---***|

"""
from __future__ import print_function


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    x_point = punct[0]
    y_point = punct[1]
    imagine[x_point][y_point] = '*'
    if x_point+1 < 6:
        if imagine[x_point+1][y_point] != '*':
            umple_forma(imagine, (x_point+1, y_point))
    if y_point+1 < 12:
        if imagine[x_point][y_point] != '*':
            umple_forma(imagine, (x_point, y_point+1))
    if x_point-1 >= 0:
        if imagine[x_point-1][y_point] != '*':
            umple_forma(imagine, (x_point-1, y_point))
    if y_point-1 >= 0:
        if imagine[x_point][y_point-1] != '*':
            umple_forma(imagine, (x_point, y_point-1))


def print_matrix(matrix):
    """Prints matrix to stdout
    """
    for row in matrix:
        row_values = "".join(row)
        print("|%s|" % row_values)
    print('\n')


def main():
    """  Main function docstring """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]

    print_matrix(imaginea)
    umple_forma(imaginea, (1, 3))
    print_matrix(imaginea)
    umple_forma(imaginea, (5, 11))
    print_matrix(imaginea)


if __name__ == "__main__":
    main()
