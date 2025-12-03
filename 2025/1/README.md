Advent of Code 2025 - Day 1
---------------------------

Secret Entrance - part 1
========================

**Passed**

Run: `python ./secret_entrance.py ./secret_entrance_input.txt`

I parse each line of the input file provided AOC.
Each line is turned into a positive or negative integer (starting with L = negative),
and then added to integer `position`.
There are 100 positions on the "dial", so each time a the value of `position`
is updated, I calculate mod of `position` and see if it's equal to 0.
If that's the case, we can add 1 to the password.


Secret Entrance - part 2
========================

**Passed**

Run: `python ./secret_entrance_revised.py ./secret_entrance_input.txt`

I slightly alter the previous code to keep track of the value of `position` BEFORE moving the "dial" (in variable `start`).
Then I calculate the `passes` over 0 and add these to the password.
There is some difficulty with two edgeases:
- When starting at position 0, and moving the dial LEFT, this is counted as a pass (since we use `math.floor()`) so we need to compensate for that.
- When ending with position 0, after moving RIGHT, this is also counted as a pass. Again we compensate.
