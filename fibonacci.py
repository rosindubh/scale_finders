# program to calculate the fibonacci sequence
# taken from youtube video
# 'https://www.youtube.com/watch?v=Qk0zUZW-U_M&index=8&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-#t=142.738937
# 15 january 2017 - phil welsby

from functools import lru_cache


@lru_cache(maxsize=1000)  # the use of this sppeds up the process
                            # by allowing python to cache the last
                            # used function. Without the function
                            # calls itself over and over. Try commenting
                            # out the line "@lru_cache" and see what happens
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print(n, ':', fibonacci(n))
