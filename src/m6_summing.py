"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Matthew De Clerck.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    cosine1 = 3
    expect1 = .13416
    actual1 = sum_cosines(cosine1)
    cosine2 = 8
    expect2 = 1.332754
    actual2 = sum_cosines(cosine2)
    cosine3 = 6
    expect3 = .724352
    actual3 = sum_cosines(cosine3)

    print('Test 1 expected:', expect1)
    print('       function:', actual1)

    print('Test 2 expected:', expect2)
    print('       function:', actual2)

    print('Test 3 expected:', expect3)
    print('       function:', actual3)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    cos = 0
    for k in range(n+1):
        cos = cos + math.cos(k)

    return cos


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    root1 = 5
    test1 = 11.854408
    equation1 = sum_square_roots(root1)
    root2 = 3
    test2 = 5.863703
    equation2 = sum_square_roots(root2)
    root3 = 7
    test3 = 19.060167
    equation3 = sum_square_roots(root3)

    print('Test 1 expected:', test1)
    print('       function:', equation1)

    print('Test 2 expected:', test2)
    print('       function:', equation2)

    print('Test 3 expected:', test3)
    print('       function:', equation3)


def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    if n < 0:
        n = -n

    sqrt = 0
    for k in range(n):
        sqrt = sqrt + math.sqrt(2*(k+1))

    return sqrt

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
