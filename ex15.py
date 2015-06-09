from sys import argv
#script is the code file I'm running. Filename is what I want to open
script, filename = argv
#txt contains the data of the file being opened "Filename or banna"
txt = open(filename)
#my string will print out my "filename" with my %r
print "Here's your file %r:" % filename
#txt will now be read and printed onto the screen
print txt.read()

txt.close()

#a string will print no action taken
print "Type the filename again:"
#raw input will wait for me to type the name of the file I want to open
file_again = raw_input ("> ")
#the file being opened will be opened
txt_again = open(file_again)
#my file will now be read and printed onto the screen
print txt_again.read()

txt_again.close()
