import numpy as np                                                    # import numpy library


ALLOWED = {1, 2, 3, 4}                                               # allowed sizes for manual input


def create_matrix(name):                                              # function to create matrix

    print(f"\nMatrix {name}")                                         # print matrix name


    while True:                                                       # loop until valid row input
        try:                                                          # try to get row input
            r = input("Enter number of rows: ").strip()              # take row input and strip spaces

            if not r:                                                 # check if input is empty
                print("Incorrect input")                             # print error message
                continue                                             # ask again

            if "." in r:                                             # check if input is decimal
                print("Incorrect input")                             # print error message
                continue                                             # ask again

            rows = int(r)                                            # convert to integer
            break                                                    # exit loop if valid

        except ValueError:                                           # if conversion fails
            print("Incorrect input")                                 # print error message


    while True:                                                      # loop until valid column input
        try:                                                         # try to get column input
            c = input("Enter number of columns: ").strip()          # take column input and strip spaces

            if not c:                                                # check if input is empty
                print("Incorrect input")                            # print error message
                continue                                            # ask again

            if "." in c:                                            # check if input is decimal
                print("Incorrect input")                            # print error message
                continue                                            # ask again

            cols = int(c)                                           # convert to integer
            break                                                   # exit loop if valid

        except ValueError:                                          # if conversion fails
            print("Incorrect input")                                # print error message


    if rows in ALLOWED and cols in ALLOWED:                         # check if size is within 1-4

        matrix = []                                                 # create empty matrix

        print(f"Enter elements for Matrix {name} (one value per line):")  # prompt for elements

        for i in range(rows):                                       # loop through each row

            print(f"  Row {i + 1}:")                               # print current row number

            row = []                                                # create empty row

            for j in range(cols):                                   # loop through each column

                while True:                                         # loop until valid element input
                    try:                                            # try to get element input
                        value = input(f"    Column {j + 1}: ").strip()   # take element input

                        if not value:                               # check if input is empty
                            print("    Please enter a value")      # print error message
                            continue                               # ask again

                        value = int(value)                         # convert to integer
                        row.append(value)                          # add value to row
                        break                                      # exit loop if valid

                    except ValueError:                             # if conversion fails
                        print("    Enter integer value only")      # print error message

            matrix.append(row)                                     # add completed row to matrix

        return np.array(matrix), rows, cols                        # return matrix and dimensions


    else:                                                           # if size exceeds 1-4

        print(f"\nMatrix size {rows}x{cols} is too large for manual input.")   # print message
        print("Switching to random fill.")                         # inform user about random fill

        while True:                                                # loop until valid min input
            try:                                                   # try to get min input
                low = input("Enter min value: ").strip()          # take min value input

                if not low:                                        # check if input is empty
                    print("Incorrect input")                       # print error message
                    continue                                       # ask again

                low = int(low)                                     # convert to integer
                break                                              # exit loop if valid

            except ValueError:                                     # if conversion fails
                print("Incorrect input")                           # print error message

        while True:                                                # loop until valid max input
            try:                                                   # try to get max input
                high = input("Enter max value: ").strip()         # take max value input

                if not high:                                       # check if input is empty
                    print("Incorrect input")                       # print error message
                    continue                                       # ask again

                high = int(high)                                   # convert to integer
                break                                              # exit loop if valid

            except ValueError:                                     # if conversion fails
                print("Incorrect input")                           # print error message

        return np.random.randint(low, high + 1, size=(rows, cols)), rows, cols   # return random matrix


A, r1, c1 = create_matrix("A")                                     # create first matrix A

B, r2, c2 = create_matrix("B")                                     # create second matrix B


print("\n----- MENU -----")                                        # print menu header
print("1. Addition")                                               # print option 1
print("2. Subtraction")                                            # print option 2
print("3. Multiplication")                                         # print option 3
print("4. Inverse of Matrix A")                                    # print option 4
print("5. Inverse of Matrix B")                                    # print option 5


try:                                                               # try to get menu choice
    choice = int(input("Enter your choice: ").strip())            # take choice input

except ValueError:                                                 # if conversion fails
    print("Incorrect input")                                       # print error message
    exit()                                                         # exit program


if choice == 1:                                                    # if user chose addition

    if A.shape == B.shape:                                         # check if shapes match
        print("\nAddition Result:")                                # print result header
        print(A + B)                                              # print addition result
    else:                                                          # if shapes dont match
        print("Addition not possible")                            # print error message
        exit()                                                     # exit program


elif choice == 2:                                                  # if user chose subtraction

    if A.shape == B.shape:                                         # check if shapes match
        print("\nSubtraction Result:")                            # print result header
        print(A - B)                                              # print subtraction result
    else:                                                          # if shapes dont match
        print("Subtraction not possible")                         # print error message
        exit()                                                     # exit program


elif choice == 3:                                                  # if user chose multiplication

    if c1 == r2:                                                   # check multiplication condition
        print("\nMultiplication Result:")                         # print result header
        print(np.matmul(A, B))                                    # print multiplication result
    else:                                                          # if condition not met
        print("Multiplication not possible")                      # print error message
        exit()                                                     # exit program


elif choice == 4:                                                  # if user chose inverse of A

    if r1 == c1:                                                   # check if matrix A is square
        try:                                                       # try to calculate inverse
            print("\nInverse of Matrix A:")                       # print result header
            print(np.round(np.linalg.inv(A), 2))                 # print inverse of A
        except np.linalg.LinAlgError:                             # if inverse doesnt exist
            print("Inverse does not exist")                       # print error message
            exit()                                                 # exit program
    else:                                                          # if matrix A is not square
        print("Matrix A is not square")                           # print error message
        exit()                                                     # exit program


elif choice == 5:                                                  # if user chose inverse of B

    if r2 == c2:                                                   # check if matrix B is square
        try:                                                       # try to calculate inverse
            print("\nInverse of Matrix B:")                       # print result header
            print(np.round(np.linalg.inv(B), 2))                 # print inverse of B
        except np.linalg.LinAlgError:                             # if inverse doesnt exist
            print("Inverse does not exist")                       # print error message
            exit()                                                 # exit program
    else:                                                          # if matrix B is not square
        print("Matrix B is not square")                           # print error message
        exit()                                                     # exit program


else:                                                              # if invalid menu choice
    print("Invalid Choice")                                        # print error message
    exit()                                                         # exit program