def quadratic_calculator():
        the_b_symbol="" # used to get the addition symbol for positive coefficient
        the_c_symbol="" # used to get the addition symbol for positive coefficient

        # Changes the user input to a float so calculations can be done and allows for decimal operation
        a_coeff= float(input('enter the coefficient of x²| a = '))
        b_coeff= float(input('enter the coefficient of x| b = '))
        c_coeff= float(input('enter the constant of the expression | c = '))

        # Automatically equates the equation to 0
        print("Assuming the quadratic equation is equal to 0")
        print()
        
        # Checks if the coefficients are positive
        if b_coeff>0:
            the_b_symbol='+'
        if c_coeff>0:
            the_c_symbol='+'
        
        # Shows the user the equation in quadratic form
        print(f"{a_coeff}x² {the_b_symbol} {b_coeff}x {the_c_symbol} {c_coeff}")
        
        # Checks if the descriminant is negative
        if (b_coeff**2)-(4*a_coeff*c_coeff)<0:
            print("The roots are imaginary")
            return
        
        # Calculates the roots for the equation
        root = ((-1*b_coeff) + ((b_coeff**2) - (4*a_coeff*c_coeff))**0.5)/2
        other_root = ((-1*b_coeff) - ((b_coeff**2) - (4*a_coeff*c_coeff))**0.5)/2

        # Checks if the roots are equal
        if root==other_root:
            print(f"x = {root}")
            return
        else:
            print(f"x = {root} or {other_root}")
            return
