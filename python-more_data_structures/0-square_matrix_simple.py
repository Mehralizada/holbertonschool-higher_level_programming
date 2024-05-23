#!/usr/bin/python3
def square_mqatrix_simple(matrix= []):
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
        return squared
