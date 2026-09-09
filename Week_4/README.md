Step-by-step debugging process for debugging_first_functions.py:
1. Running the program first causes an error message:
  File "d:\AAISE-2026-27\Python_Programming\Week_4\debugging_first_functions.py", line 11
    if denominator = 0: #bugged change: should be "==" for comparison, but instead writing "=" causes a syntax error.
       ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

2. To fix, follow the advice of SyntaxError and replace the single = with a double ==. 
Note: When initially creating this bug, the AI recommended I change the single = into a <=. This would not be what I want; I am explicitly returning the error message with "denominator cannot be zero", not "denominator cannot be zero or below". If the denominator value was negative, my program would still run exactly as intended. 

3. After fixing the first syntax error bug, I run into the second bug (that I added): my print value after entering the numerator and denominator is way too high! 

4. To find the source of this bug, I added a print command at the end of the code to show the result of combining the numerator and dominator, which gave the information that the two user inputs are adding before multiplying by 100 and not delineating separately. 

5. To fix the bug, I (re-)changed the symbol in the first function between the "return numerator + denominator" from a "+" to a ",". Then, at the end of the code, I removed the "1" value from the denominator, allowing the result to be formed properly from the two user input floats.