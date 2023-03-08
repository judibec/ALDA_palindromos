from functions import palindome_solutions as ps
from execution import timeExecution as te

if __name__ == '__main__':
    table = te.takeTimes(10000000)
    for row in table:
        print(row)


