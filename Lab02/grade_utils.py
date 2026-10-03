"""Module helper for reporting students grades"""


def letter_grade(gpa):
    """This module is used for calculating the student's grade from GPA"""
    # TODO: your if/elif chain here
    if gpa == 5.00:
        return "A+"
    elif gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
