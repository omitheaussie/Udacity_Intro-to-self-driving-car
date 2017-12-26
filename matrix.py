import math
from math import sqrt
import numbers
from copy import deepcopy

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
def dot_product(vector_one, vector_two):
        dp=0
        if len(vector_one)==len(vector_two):
            for i in range(len(vector_one)):
                dp=dp+vector_one[i]*vector_two[i]
        return dp

def get_row(matrix, row):
    return matrix[row]
                                                                         
def get_column(matrix, column_number):
    column = [row[column_number] for row in matrix]
    return column
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here - COMPLETED
        if self.h==1:
            ans=self.g[0][0]
        if self.h>1:
            ans = (self.g[0][0]*self.g[1][1])-(self.g[0][1]*self.g[1][0])
        
        print(ans)
        return ans

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        trace_sum=0
        # TODO - your code here - COMPLETED
        for i in range(self.h):
            trace_sum=trace_sum+self.g[i][i]
        
        return trace_sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        #print(self.g)
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        inverse=zeroes(self.h,self.w)
        if len(self.g)==1:
            inverse.g[0][0]=1.0/self.g[0][0]
            return inverse
        
        # TODO - your code here - COMPELTED
        denom=self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
        if denom==0:
            raise ValueError('The denominator of a fraction cannot be zero')
                                                                         
        if len(self.g)>=2:
            f = 1/(denom)
            inverse.g[0][0] = self.g[1][1]*f
            inverse.g[0][1] = -self.g[0][1]*f
            inverse.g[1][0] = -self.g[1][0]*f
            inverse.g[1][1] = self.g[0][0]*f
        return inverse
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here - COMPLETED
        matrix_transpose=zeroes(self.w,self.h)
        #print(self.g)
        if len(self.g)>1:
            for i in range(len(self.g[0])):
                for j in range(len(self.g)):
                    matrix_transpose.g[i][j]=self.g[j][i]
                    
        if len(self.g)==1:
            matrix_transpose.g[0][0]=self.g[0][0]
            matrix_transpose.g[1][0]=self.g[0][1]
        
        #print(matrix_transpose.g)
        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = zeroes(self.h,self.w)

        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                matrixSum.g[i][j]=self.g[i][j]+other.g[i][j]
        return matrixSum #self
                                                                         
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        neg_self=deepcopy(self)

        for i in range(self.h):
            for j in range(self.w):
                neg_self.g[i][j]=self.g[i][j]*(-1)

        return neg_self
                                                                         
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        neg_other=-self
        return (self+neg_other)
                                                                         
    
                                                                         
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        result = zeroes(self.h,other.w)
        row_result = []
    
        for m in range(len(self.g)):
            r=get_row(self.g, m)
            for p in range(len(other.g[0])):
                c=get_column(other.g,p)
                result.g[m][p]=dot_product(r,c)
                                                                         
        return result

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """

        rmul_matrix=zeroes(self.h,self.w)
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            for i in range(self.h):
                for j in range(self.w):
                    rmul_matrix.g[i][j]=self.g[i][j]*other

        return rmul_matrix