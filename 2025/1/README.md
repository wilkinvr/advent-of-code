Advent of Code 2025 - Day 1
---------------------------

Secret Entrance
===============

**Passed**

Run: `python ./secret_entrance.py ./secret_entrance_input.txt`

I parse each line of the input file provided AOC.
Each line is turned into a positive or negative integer (starting with L = negative),
and then added to integer `position`.
There are 100 positions on the "dial", so each time a the value of `position`
is updated, I calculate mod of `position` and see if it's equal to 0.
If that's the case, we can add 1 to the password.
