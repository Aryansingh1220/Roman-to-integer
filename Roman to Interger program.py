class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2*rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
print("------------------------------------------------------")
print(" ")
print("CONVERTER TO CONVERT ROMAN TO INTEGER")
print(" ")
print("------------------------------------------------------")
n=input("Please enter only roman numbers here: ")
if n.isalpha()==True:
   print("Your Integral value is: ",py_solution().roman_to_int(n))
else:
   print("Please enter only roman value")
   n=input("Please enter roman number here: ")
   if n.isalpha()==True:
        print("Your Integral value is: ",py_solution().roman_to_int(n))
   else:
        print("You are not using Roman Numbers")
        print("Program Terminated.")
        print("Please execute again and use Roman value only.")


