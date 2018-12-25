

def main():
    # 0 stands for empty space
    # easy
    sudoku1 = "000260701" \
             "680070090" \
             "190004500" \
             "820100040" \
             "004602900" \
             "050003028" \
             "009300074" \
             "040050036" \
             "703018000"

    # about as hard as it gets
    sudoku = "020000000" \
             "000600003" \
             "074080000" \
             "000003002" \
             "080040010" \
             "600500000" \
             "000010780" \
             "500009000" \
             "000000040"

    solved = iterate(sudoku, -1, 1)
    printSudoku(solved)


def iterate(sudoku, index, number):

    # check the sudoku, return None if wrong
    # index == 1 means first iteration, no need to check
    if index != -1:
        sudoku = sudoku[:index] + str(number) + sudoku[index+1:]
        if not checkAll(sudoku, index):
            return None

    # if sudoku is done
    if index >= 80:
        return sudoku

    # if the next number isnt a zero, skip it
    if sudoku[index+1] != '0':
        return iterate(sudoku, index+1, sudoku[index+1])

    # run through the numbers for the next row
    # print(str(index) + " fun")
    nextNumber = 1
    while nextNumber < 10:
        result = iterate(sudoku, index+1, nextNumber)
        # if not wrong, return the result
        if result is not None: return result
        else:
            nextNumber += 1
    # return none if the sudoku can not be solved
    return None


# check the row the index is in
def checkRow(sudoku, index):
    if sudoku[index] == '0': return True
    rowNumber = int(index/9)
    for i in range(9):
        if i == index%9:
            continue
        if sudoku[rowNumber*9+i] == sudoku[index]:
            return False
    return True


# check the column the index is in
def checkColumn(sudoku, index):
    if sudoku[index] == '0':
        return True
    columnNumber = index % 9
    for loc in range(columnNumber, 81, 9):
        if loc == index:
            continue
        if sudoku[loc] == sudoku[index]:
            return False
    return True


# the the square the index is in
def checkSquare(sudoku, index):
    if sudoku[index] == '0': return True
    # top left of square
    start = int(index / 27)*27 + int((index % 9) / 3) * 3
    for i in range(3):
        for j in range(3):
            loc = start+ i*9 + j
            if loc == index:
                continue
            if sudoku[loc] == sudoku[index]:
                return False
    return True


# check the row, column and square the index is in
def checkAll(sudoku, index):
    return checkColumn(sudoku, index) and checkRow(sudoku, index) and checkSquare(sudoku, index)


# print the sudoku
def printSudoku(sudoku):
    for i in range(9):
        row = ""
        for j in range(9):
            row += sudoku[9*i+j]
        print(row)


if __name__ == '__main__':
    main()
