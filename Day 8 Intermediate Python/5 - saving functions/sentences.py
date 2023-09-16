#Import any individual functions from outside packages 
#that are used in your functions.
#These are called dependencies.
from statistics import mean
from statistics import median

#Function definitions with docstrings
def printMean(a_list):
	'''Returns the mean of a list, rounded to the hundredths, in a complete sentence.'''
	m = mean(a_list)
	return f"The mean of the numbers provided is {round(m, 2)}."
	
def printSum(a_list):
	'''Returns the sum of a list in a complete sentence.'''
	s = sum(a_list)
	return f"The sum of the numbers provided is {s}."
	
def printMedian(a_list):
	'''Returns the median of a list in a complete sentence.'''
	m = median(a_list)
	return f"The mean of the numbers provided is {m}."

#This if statement should be included at the end of any module
#If you don't include this, when you import the module, it will run
#the module script from top to bottom instead of only importing the
#functions	
if __name__ == "__main__":
	main()