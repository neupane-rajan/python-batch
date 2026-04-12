math = {"a","b","c","d","z","y"}
science = {"a","b","e","f","g"}

# common students

s_and_m = math & science

# aauta matra subject padne student
only_one_subject = math^science
print(only_one_subject)
# only science
o_s = science-math
print(o_s)
# only math
o_m = math-science
print(o_m)


# all students

all_students = math | science
print(all_students)