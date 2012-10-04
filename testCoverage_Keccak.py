# The Keccak sponge function, designed by Guido Bertoni, Joan Daemen,
# Michael Peeters and Gilles Van Assche. For more information, feedback or
# questions, please refer to our website: http://keccak.noekeon.org/
# 
# Implementation by Renaud Bauvin,
# hereby denoted as "the implementer".
# 
# To the extent possible under law, the implementer has waived all copyright
# and related or neighboring rights to the source code in this file.
# http://creativecommons.org/publicdomain/zero/1.0/


import Keccak
import cProfile

def runCoverage(b):
	
	A=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	
	for b in  [25, 50, 100, 200, 400, 800, 1600]:
	
		myKeccak=Keccak.Keccak(b)	
		myKeccak.KeccakF(A, True)
	
	myKeccak.printState(A,'Final result')

	
runCoverage()
