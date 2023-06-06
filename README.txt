This file is to build CLI which is similar to the idead of REPL 

use jupyter-lab to add data!

➜  PA03 git:(main) ✗ pytest
===================================== test session starts ==================================================================================
platform darwin -- Python 3.9.1, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/tristaed/Desktop/my-repo/python-practice/PA03
plugins: anyio-3.6.2
collected 2 items                                                                                                                                                                       

test_transaction.py ..                                                                                             [100%]

=============================================================== 2 passed in 0.07s ==========================================

➜  PA03 git:(main) ✗ python -m pylint tracker.py
************* Module tracker
tracker.py:7:32: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:23:0: C0301: Line too long (133/100) (line-too-long)
tracker.py:35:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
tracker.py:52:44: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:61:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:62:0: C0304: Final newline missing (missing-final-newline)
tracker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tracker.py:11:7: R1714: Consider merging these comparisons with "in" to "arglist in ([], ['menu'])" (consider-using-in)
tracker.py:23:12: C0103: Variable name "userInput" doesn't conform to snake_case naming style (invalid-name)
tracker.py:31:12: C0103: Variable name "userInput" doesn't conform to snake_case naming style (invalid-name)
tracker.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:43:8: W0105: String statement has no effect (pointless-string-statement)
tracker.py:4:0: C0411: standard import "import sys" should be placed before "from transaction import Transaction" (wrong-import-order)

-----------------------------------
Your code has been rated at 7.05/10