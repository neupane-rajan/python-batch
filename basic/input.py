
# note : if we try to convert boolean data type into integer then true convert into "1" and false convert into "0";
# but if we try to convert none data type into integer then it will raise an error.
# but if we try to convert all data type into string then it will convert without error.

num1 = "12"
num2 = "21"
name = "rajan"
roll_no = 21
bool_type  = True
# none_type = None

con_int1 =int(bool_type) 
# con_int2 =int(none_type) 
 
print(f"boolean converison: {con_int1}")

