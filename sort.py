#sort.py #done
#comments are written on line they apply to


def sort(fileName):	#defining function
	homo = 0					#variable initialization
	hetero = 0	
	for line in fileName:		#for loop that checks each line
													#easy way to split up each line
		A, B, C, D, E, F = line.split()			
		if E==F:			#checks if letters are the same
			homo+=1			#adds a count to the "same" category
		else:					#checks if letters are different
			hetero+=1		#adds a count to "different" category
		# print(line)		
		# print(A)
		# print(B)			
		# print(C)			# these can be used to print each 											# "column" of genetic data
		# print(D)
		# print(E)
		# print(F)
		# print("\n")
		
		#final print statement to compare two categories
	print('Homozygous= '+str(homo), 'Heterozygous= '+str(hetero))

#function asks for input (which file to open and read)
#upon entering filename (with .txt or .tped extention), function will be called with filename as argument
sort(fileName=open(raw_input("What's the name of the file? "), "r"))
