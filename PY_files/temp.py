temp=input("Enter the temp need to convert like eg : 34F or 67C")
degree = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper()=='C':
    NUM1=int(round((9*degree)/5+32))
    o_convention = 'FArenheit'
elif i_convention.upper()=='F':
    NUM1=int(round((degree-32)*5/9))
    o_convention = 'celsius'
else:
  print("Input proper convention.")
  #quit()
print("The temperature in", o_convention, "is", NUM1, "degrees.")
