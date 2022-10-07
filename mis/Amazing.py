# imports
import random

################################################################################
# init2dArray
# Function to create a 2 dimensional array of values. This function creates an
# List of Lists to accomplish this. Each element in the list can be accedd like
# x, y grid coordinates with the notation of array[x][y]. This would access the
# List at index x and the element at index y of that list. This same element can
# also be accessed as array[x].index(y)
#
#       x: The number of elements in the x dimension of the array.
#       y: The number of elements in the y dimension of the array.
#   value: The value to initialize each element with.
#
# returns: A new List with x elements. Each one a list with a y number of 
#          elements. All elements are initialized with the value passed in.

def init2dArray(x, y, value = ''):
	array2d = []
	for i in range(x):
		array2d.append([])
		for j in range(y):
			array2d[i].append(value)
	
	return array2d

################################################################################
# Main program entry point

def main():
	h = 0
	w = 0

	while(h < 2 and w < 2):
		h, w = input("What are your width and length (width,length): ").split(',')
		h = int(h)
		w = int(w)
		if h < 2 and w < 2:
			print("Meaningless dimensions. Try again.")
	V = init2dArray(h, w)
	U = init2dArray(h, w)
	print("\n\n\n\n")
	Q = 0
	Z = 0
	# Print the top row
	X = random.randint(1, h)
	for I in range(h):
		if I == X:
			print(".  ")
		else:
			print(".--")
	#endLoop
	print(".")
	C = 1
	V[X][1] = C
	C += 1
	#200
	R = X
	S = 1
	if R - 1 == 0 or V[R - 1][S] != 0: #260/265
		if S - 1 == 0 or V[R][S - 1] != 0: #530/540
			if R == h or V[R+1][S] != 0: #670/680
				if S != w: #740
					if V[R][S + 1] != 0: #760
						#780: GOTO 1000
						#1000: GOTO 210
						while R != h: #210
							R += 1 #240
							if V[R][S] == 0: #250
								continue #GOTO 210
							else:
								if R - 1 == 0: #260
									if S - 1 == 0: #530
										if R == h: #670
											if S != w: #740
												if V[R][S+1] != 0: #760
													continue #GOTO 780
												else:
													if Q == 1: #910
														Z = 1 #960
														if w[R][S] == 0: #970
															w[R][S] = 1 #980
															Q = 0
															R = 1
															S = 1
															#TODO: GOTO 250
														else:
															w[R][S] = 3 #975
															Q = 0
															continue #GOTO 1000
													else:
														V[R][S+1] = C #920
														C += 1
														if w[R][S] == 0:
															w[R][S] = 1 #940
															S += 1 #950
															if C == h * w + 1:
																for J in range(w): #1010
																	print("I") #1011
																	for I in range(h): #1012
																		if w[I][J] < 2: #1013
																			print("  I") #1030
																		else:
																			print("   ") #1020
																	print("\n") #1041
																	for I in range(h): #1043
																		if w[I][J] == 0 or w[I][J] == 2: #1045/1050
																			print(":--") #1060
																		else:
																			print(":  ") #1051
																	print(".")#1071
																	#1073 END
															#else: GOTO 260
														else:
															w[R][S] = 3 #930
															#GOTO 950
											else:
												if Z == 1: #750
													continue #GOTO 780
												else:
													Q = 1 #755

		elif R == h or V[R + 1][S] != 0:
			#610
			if S != w:
				#630
				if V[R][S + 1] != 0:
					#660 - goto 820
					#820
					V[R][S - 1] = C
					C += 1
					#840
				else:
					#640
					X = random.randint(1, 2)
					#650
			elif Z == 1:
				#660 - goto 820
				#820
				V[R][S - 1] = C
				C += 1
				#840
			else:
				Q = 1
				#640
				X = random.randint(1, 2)
				#650
		elif S != w:
			#560
			if V[R][S + 1] != 0:
				#590
				X = random.randint(1, 2)
				#600
			else:
				#570
				X = random.randint(1, 2)
				#580
		elif Z == 1:
			#590
			X = random.randint(1, 2)
			#600
		else:
			Q = 1
			#570
	#270/280
	elif S - 1 == 0 or V[R][S - 1] != 0:
		if R == h:
			if S != w:
				if V[R][S + 1] != 0:
					V[R - 1][S] == C
					C += 1
					U[R - 1][S] = 2
					R -= 1
					if C == h * w + 1:
						for J in range(w):
							print("I")
							for I in range(h):
								if U[I][J] < 2:
									print("  I")
								else:
									print("   ")
							print("\n")
							for I in range(h):
								if U[I][J] == 0 or U[I][J] == 2:
									print(":--")
								else:
									print(":  ")
							print(".")
	#290/300
	elif R == h or V[R + 1][S] != 0:
		#330
		if S != w:
			#340
			if V[R][S + 1] != 0:
				#370
				X = random.randint(1, 2)
				#380
		elif Z == 1:
			#370
			X = random.randint(1, 2)
			#380
		else:
			Q = 1
			#350
	#310
	else:
	   X = random.randint(1, 3)
	   #320

################################################################################
# Call main program

main()