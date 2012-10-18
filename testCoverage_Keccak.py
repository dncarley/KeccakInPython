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

def runCoverage():
	"""
		Simple coverage test.  Currently executing at 37% line coverage.
	"""

	A=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

	# cover normal and verbose on all nominal b-values
	for b in  [25, 50, 100, 200, 400, 800, 1600]:	
		myKeccak=Keccak.Keccak(b)	
		myKeccak.KeccakF(A, False)
	for b in  [25, 50, 100, 200, 400, 800, 1600]:	
		myKeccak=Keccak.Keccak(b)	
		myKeccak.KeccakF(A, False)	
	
	#assert coverage on only permitted setB 
	myKeccak=Keccak.Keccak(25)
	try:
		myKeccak.setB(1)
	except:
		pass
	myKeccak.setB(1600)
	myKeccak.KeccakF(A, False)		
	
	#
#	myKeccak = Keccak.Keccak(r=1024,c=576,n=1024,verbose=False)
	myKeccak = Keccak.Keccak(1600)
	print myKeccak.Keccak('1')

		
def runSimple(v):
	myKeccak=Keccak.Keccak(25)	
	myKeccak.KeccakF(v, False)	



A=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
B=[[1,0,0,0,0],[0,0,0,0,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

command = 'runSimple(%s)' % A
cProfile.run(command)
command = 'runSimple(%s)' % B
cProfile.run(command)


cProfile.run('runCoverage()')

