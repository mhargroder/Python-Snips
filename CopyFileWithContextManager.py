#This snip is quick way to create a copy of a file using a context manager
#acknowledgements: Corey Schafer (coreyms.com)

with open('test.txt','r') as f:
	with open('testCopy.txt', 'w') as fc:
		for line in f:
			fc.write(line)



