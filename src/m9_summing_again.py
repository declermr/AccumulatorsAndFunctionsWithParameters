"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Matthew De Clerck.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    integer1 = 4
    power1 = 3
    expected1 = 100
    actual1 = sum_powers(integer1, power1)
    integer2 = 7
    power2 = 2
    expected2 = 140
    actual2 = sum_powers(integer2, power2)
    integer3 = 5
    power3 = 4
    expected3 = 979
    actual3 = sum_powers(integer3, power3)

    print('Test 1 expected:', expected1)
    print('       actual:  ', actual1)
    print('Test 2 expected:', expected2)
    print('       actual:  ', actual2)
    print('Test 3 expected:', expected3)
    print('       actual:  ', actual3)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    power = 0
    for k in range(n):
        power = power + (k + 1) ** p

    return power


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    initial1 = 4
    final1 = 7
    power1 = 3
    expected1 = 748
    actual1 = sum_powers_in_range(initial1, final1, power1)
    initial2 = 6
    final2= 10
    power2 = 2
    expected2 = 330
    actual2 = sum_powers_in_range(initial2, final2, power2)
    initial3 = 3
    final3 = 9
    power3 = 4
    expected3 = 15316
    actual3 = sum_powers_in_range(initial3, final3, power3)

    print('Test 1 expected:', expected1)
    print('       actual:  ', actual1)
    print('Test 2 expected:', expected2)
    print('       actual:  ', actual2)
    print('Test 3 expected:', expected3)
    print('       actual:  ', actual3)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    powerrange = 0
    for k in range(n - m + 1):
        powerrange = powerrange + (k + m) ** p

    return powerrange


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
