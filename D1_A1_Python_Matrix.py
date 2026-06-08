# Import numpy library for matrix operations
import numpy as np

# Function to take rows and columns of matrix
def get_size(name):

    # Display matrix name
    print(f"\nMatrix {name}")

    # Keep asking until valid input
    while True:

        try:

            # Take rows input as string
            r = input("Rows: ")

            # Take columns input as string
            c = input("Columns: ")

            # Check if input is empty or decimal value
            if "." in r or "." in c or r == "" or c == "":

                # Show error message
                print("Incorrect input")

                # Restart loop
                continue

            # Convert rows string into integer
            r = int(r)

            # Convert columns string into integer
            c = int(c)

            # Check rows and columns are positive
            if r <= 0 or c <= 0:

                # Show error
                print("Incorrect input")

                # Restart loop
                continue

            # Return valid rows and columns
            return r, c

        # Runs when conversion fails
        except ValueError:

            # Show error message
            print("Incorrect input")

# Function to create matrix
def create_matrix(name, r, c):

    # Check matrix size
    # If rows and columns are <=4 then take manual input
    if r <= 4 and c <= 4:

        # Display matrix name
        print(f"\nEnter Matrix {name}")

        # Create empty list for storing matrix
        data = []

        # Loop for rows
        for i in range(r):

            # Create empty row
            row = []

            # Loop for columns
            for j in range(c):

                # Keep asking until correct value
                while True:

                    try:

                        # Take element input
                        value = int(input(f"Row {i+1} Col {j+1}: "))

                        # Add value into row
                        row.append(value)

                        # Stop input loop
                        break

                    # If user enters non-integer
                    except ValueError:

                        # Display error
                        print("Enter integer only")

            # Add completed row into matrix
            data.append(row)

        # Convert list into numpy array
        return np.array(data)

    # If matrix size is greater than 4x4
    else:

        # Inform user
        print("Size greater than 4x4, random values generated")

        # Take minimum random value
        low = int(input("Minimum value: "))

        # Take maximum random value
        high = int(input("Maximum value: ") )

        # Generate random matrix
        return np.random.randint(
            low,
            high + 1,
            (r,c)
        )

# Loop for checking matrix sizes
while True:

    # Run loop maximum 3 times
    for i in range(3):

        # Take Matrix A size
        r1, c1 = get_size("A")

        # Take Matrix B size
        r2, c2 = get_size("B")

        # Check both matrices have same size
        if r1 == r2 and c1 == c2:

            # Stop for loop
            break

        # If sizes are different
        print("Incorrect input")

        # Explain reason
        print("Both matrices must have same rows and columns")

    # If 3 attempts completed
    else:

        # Show message
        print("Maximum attempts reached")

        # Stop program
        exit()

    # Exit while loop
    break

# Create Matrix A
A = create_matrix("A",r1,c1)

# Create Matrix B
B = create_matrix("B",r2,c2)

# Infinite loop for menu
while True:

    # Display operations
    print("""
----- MENU -----
1. Addition
2. Subtraction
3. Multiplication
4. Inverse A
5. Inverse B
6. Exit
""")

    try:

        # Take user choice
        choice = int(
            input("Choice: ")
        )

    # If wrong input
    except ValueError:

        # Display error
        print("Incorrect input")

        # Restart menu
        continue

    # Addition operation
    if choice == 1:

        # Add matrices
        print(A + B)

    # Subtraction operation
    elif choice == 2:

        # Subtract matrices
        print(A - B)


    # Multiplication operation
    elif choice == 3:

        # Check multiplication condition
        if c1 == r2:
            # Multiply matrices
            print(np.matmul(A,B))

        # If multiplication condition fails
        else:
            print("Multiplication not possible")

    # Inverse of Matrix A
    elif choice == 4:

        # Check square matrix
        if r1 == c1:

            try:

                # Calculate inverse
                print(np.round(np.linalg.inv(A),2))

            # If inverse does not exist
            except:

                print(
                "Inverse does not exist"
                )

        # If not square
        else:
            print("Matrix A not square")


    # Inverse of Matrix B
    elif choice == 5:

        # Check square matrix
        if r2 == c2:

            try:

                # Calculate inverse
                print(np.round(np.linalg.inv(B),2))

            # If inverse does not exist
            except:
                print("Inverse does not exist")

        # If not square
        else:
            print("Matrix B not square")


    # Exit option
    elif choice == 6:

        # Display exit message
        print("Program exited")

        # Stop menu loop
        break

    # Invalid menu option
    else:
        # Display error
        print("Invalid choice")