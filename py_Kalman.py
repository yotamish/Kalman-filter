# not finished!

import numpy
from numpy import dot

def predict(X,P,A,Q,B,U):
	X = dot(A,X) + dot(B,U)
	P = dot(A, dot(P,A.T)) + Q
	return (X,P)

