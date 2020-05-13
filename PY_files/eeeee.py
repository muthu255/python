# Ask the user to enter the names of files to compare
fname1 = input("Enter the first filename: ")
fname2 = input("Enter the second filename: ")

# Open file for reading in text mode (default mode)
f1 = open(fname1)
f2 = open(fname2)


print("-----------------------------------")
print("Comparing files ", " > " + fname1, " < " +fname2, sep='\n')
print("-----------------------------------")


f1_line = f1.readline()
f2_line = f2.readline()


line_no = 1

# Loop if either file1 or file2 has not reached EOF
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
   
   
 
    if f1_line != f2_line:
       
       
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)
     
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)
           
 
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)
       
        elif f2_line != '':
            print("<", "Line-%d" %  line_no, f2_line)

   
        print()
    if  f1_line == f2_line:
        print("=", "Line-%d" % line_no, "Pass")
    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()

   

   
    line_no += 1

f1.close()
f2.close()
