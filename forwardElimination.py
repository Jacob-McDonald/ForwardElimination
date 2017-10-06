def naiveForwardElimination(*args,catOut=False,catIn=False):

    A = args[0]
    b = args[1]

    num_rows = A.shape[0]
    num_columns = A.shape[1]

    for column in range(0,num_columns-1):

        for row in range(column+1,num_rows):

            xmult = A[row,column]/A[column,column]

            for column_row_sweep in range(0,num_rows):

                A[row,column_row_sweep] = A[row,column_row_sweep]-xmult*A[column,column_row_sweep]

                if len(args) == 2:

                    b[row] = b[row]-xmult*b[column]





    if len(args) == 2:

        if catOut == False:

            return A,b

        if catOut == True:

            return np.c_[A,b]

    elif len(args) == 1 and catIn == True:

        if catOut == True:

            return A

        if catOut == False:

            return [A[:,0:num_columns], A[:,num_columns]]

    else:

        return A

def ppForwardElimination(*args,catOut=False,catIn=False):