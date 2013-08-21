1. Write a program to generate a following structure:
	******
	******
	******
	******
	******
	******

  Solution:
    def pyramid(rows):
	    for i in range(rows):
		    print("*" * rows)

    pyramid(6)


2. Write a program to generate a following structure:
	******
	*****
	****
	***
	**
	*
  Solution:
  	def pyramid(rows):
			for i in range(rows):
				print("*" * (rows-i))

		pyramid(6)
		
3. Write a program to generate a following structure:
	*
	**
	***
	****
	*****
 Solution:
 
	def pyramid(rows):
		for i in range(rows):
			print ("*"*(i+1))
	pyramid(6)


4. Write a program to generate a following structure:
	     *
	    ***
	   *****
	  *******
	 *********
	***********
 Solution:
 	def pyramid(rows):
		for i in range(rows):
			print ' '*(rows-i-1) + '*'*(2*i+1)
		
	pyramid(6)
	

5. Write a program to generate a following structure:
	
		******
		 *****
		  ****
		   ***
		    **
	     	     *
	 Solution:
	 	def pyramid(rows):
			for i in range(rows):
				print ' '*(i) + '*'*(rows-i)

		pyramid(6)
