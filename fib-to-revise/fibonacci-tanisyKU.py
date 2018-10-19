# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

  def fib(n):
    if n == 0:
        return 0
    else:
        (a, b) = (0, 1)
        for i in range(n ):
            (a, b) = (b, a + b)
        return b
    

print(fib(2018))