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
