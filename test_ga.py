import numpy

from ga import cal_pop_fitness

def test_cal_pop_fitness():
    pop = numpy.array([[1, 2, 3, 4, 5],
                       [2, 3, 4, 5, 7],
                       [-1, 3, 25, 2, 6],
                       [2, 3, 3, 5, 6],
                       [2, 2, 4, -2, 6]])

    equation_inputs = numpy.array([2, 5, 8, 3, 1])

    result = numpy.array([53, 73, 225, 64, 46])

    assert (cal_pop_fitness(equation_inputs, pop) == result).all()