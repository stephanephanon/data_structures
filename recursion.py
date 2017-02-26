"""
Recursion examples from Lewis and Chase
"""
from functools import wraps
import logging


logger = logging.getLogger(__name__)


def memoize_class(f):
    """
    Memoization decorator
    Saves result from method calls in local cache
    Will save results across class instances
    """
    cache = {}

    @wraps(f)
    def inner(self, *args, **kwargs):
        """
        Return the function return value for this set
        of args and kwargs. Cache if new function call.
        :return: function return
        """
        # this is a simple key but it should be good enough here
        cache_key = (f.__name__, args, frozenset(sorted(kwargs.items())))

        if cache_key not in cache:
            logger.debug("Cache miss. Add {0}, {1} to cache."
                         .format(args, kwargs))
            cache[cache_key] = f(self, *args, **kwargs)
        return cache[cache_key]
    return inner


def memoize_instance(f):
    """
    Instance memoization decorator
    Saves result from method calls in local cache
    Will save results for all calls of this instance
    """
    @wraps(f)
    def inner(self, *args, **kwargs):
        """
        Return the function return value for this set
        of args and kwargs. Cache if new function call.
        :return: function return
        """
        cache_name = '__memo_cache__'
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})
        cache = getattr(self, '__memo_cache__')
        cache_key = (f.__name__, args, frozenset(sorted(kwargs.items())))

        if cache_key not in cache:
            logger.debug("Cache miss. Add {0}, {1} to cache."
                         .format(args, kwargs))
            cache[cache_key] = f(self, *args, **kwargs)
        return cache[cache_key]
    return inner


# -------------------------
# Towers of Hanoi Example
# -------------------------
class TowersOfHanoi(object):
    """
    Recursive towers of hanoi solver that prints
    out human-readable instructions.  Goal is to
    move all of the disks on peg 1 to peg 3.
    Rules are:
    -- all of the disks start on peg 1, stacked large
    to small from bottom to top
    -- 3 pegs, N number of disks of different sizes
    -- small disk can go on large, but not vice versa
    -- any size disk can go on an empty peg
    """
    def _move_one_disk(self, start_tower, end_tower):
        """
        Move one disk from start tower to end tower
        :param start_tower: starting tower (begin move from here)
        :param end_tower: ending tower (end move here)
        :return: instruction on how to move from start to end
        """
        instruction = ("Move one disk from {0} to {1}"
                       .format(start_tower, end_tower))
        return instruction

    def _move_disks(self, number_of_disks,
                    start_tower, end_tower,
                    temporary_tower):
        """
        Move the number of disks specified between
        start_tower and end_tower
        :param number_of_disks: number of disks
        :param start_tower: starting tower (begin move from here)
        :param end_tower: ending tower (end move here)
        :param temporary_tower: middle tower on the way to end
        :return: list of instruction strings
        """
        instructions = []
        if number_of_disks == 1:
            # base case
            instructions = [self._move_one_disk(start_tower, end_tower)]
        else:
            # recurse
            instruction_one = self._move_disks(number_of_disks-1,
                                               start_tower=start_tower,
                                               end_tower=temporary_tower,
                                               temporary_tower=end_tower)
            logger.debug("INSTRUCTION ONE: {}".format(instruction_one))

            instruction_two = [self._move_one_disk(start_tower, end_tower)]
            logger.debug("INSTRUCTION TWO: {}".format(instruction_two))

            instruction_three = self._move_disks(number_of_disks-1,
                                                 start_tower=temporary_tower,
                                                 end_tower=end_tower,
                                                 temporary_tower=start_tower)
            logger.debug("INSTRUCTION THREE: {}".format(instruction_three))

            instructions.extend(instruction_one)
            instructions.extend(instruction_two)
            instructions.extend(instruction_three)

        return instructions

    def solve(self, number_of_disks):
        """
        Solve the towers of hanoi problem for
        self.number_of_disks disks
        :number_of_disks: number of disks for solver
        :return: list of instruction strings
        """
        return self._move_disks(number_of_disks,
                                start_tower=1, end_tower=3, temporary_tower=2)


class MemoizedTowersOfHanoi(TowersOfHanoi):
    """
    Recursive towers of hanoi solver that prints
    out human-readable instructions.  Goal is to
    move all of the disks on peg 1 to peg 3.

    Includes memoization of the disk moving functions
    to cut down on number of repeated calls

    Rules are:
    -- all of the disks start on peg 1, stacked large
    to small from bottom to top
    -- 3 pegs, N number of disks of different sizes
    -- small disk can go on large, but not vice versa
    -- any size disk can go on an empty peg
    """
    @memoize_instance
    def _move_one_disk(self, start_tower, end_tower):
        return super(MemoizedTowersOfHanoi, self)._move_one_disk(start_tower, end_tower)

    @memoize_instance
    def _move_disks(self, number_of_disks,
                    start_tower, end_tower,
                    temporary_tower):
        return super(MemoizedTowersOfHanoi, self)._move_disks(number_of_disks,
                                                              start_tower,
                                                              end_tower,
                                                              temporary_tower)


# -------------------------
# N-Factorial Example
# -------------------------
class NFactorial(object):
    """
    Calculate n! = n*n-1*n-2...*2*1
    """
    def _n_factorial(self, n):
        if n == 1:
            # base
            return 1
        else:
            # recurse
            return n * self._n_factorial(n-1)

    def __call__(self, n):
        """
        Shortcut callable for n-factorial
        :param n:
        :return: n factorial
        """
        if n < 1:
            return 0
        return self._n_factorial(n)

    def solve(self, n):
        """
        Return n!
        :param n:
        :return: n factorial
        """
        if n < 1:
            return 0
        return self._n_factorial(n)


class MemoizedNFactorial(NFactorial):
    """
    Calculate n! = n*n-1*n-2...*2*1
    Includes memoization of the multiplication
    to cut down on number of repeated calls
    """
    @memoize_instance
    def _n_factorial(self, n):
        return super(MemoizedNFactorial, self)._n_factorial(n)


# -------------------------
# sum(N) Example
# -------------------------
class SumNTo1(object):
    """
    Calculate sum of integers from N to 1
    """
    pass

class MemoizeSumNTo1(object):
    """
    Calculate sum of integers from N to 1
    """
    pass


# -------------------------
# Fibonacci Example
# -------------------------
class Fibonacci(object):
    """
    Calculate fibonacci sequence at f(n)
    """
    def _fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self._fibonacci(n-1) + self._fibonacci(n-2)

    def __call__(self, n):
        if n < 0:
            return 0
        return self._fibonacci(n)

    def solve(self, n):
        if n < 0:
            return 0
        return self._fibonacci(n)


class MemoizedFibonacci(Fibonacci):
    """
    Calculate fibonacci sequence
    Includes memoization of the function calls
    to cut down on number of repeated calls
    """
    @memoize_instance
    def _fibonacci(self, n):
        return super(MemoizedFibonacci, self)._fibonacci(n)
