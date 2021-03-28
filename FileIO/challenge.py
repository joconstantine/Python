
with open("sample.txt", 'ta') as times_table:
    for i in range(1, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=times_table)
        print("-" * 20, file=times_table)
