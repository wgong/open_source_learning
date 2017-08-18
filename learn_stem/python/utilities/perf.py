import timeit
print(timeit.timeit('"-".join(str(n) for n in range(1000))', number=10000))
print(timeit.timeit('for n in range(1000): n*n*n', number=10000))
"""
toshiba laptop:
6.5739352509028635
2.1101508438248997
"""