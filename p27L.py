def sort_dict_by_keys(input_dict, reverse=False):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[0], reverse=reverse))
    return sorted_dict

def sort_dict_by_values(input_dict, reverse=False):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict

def main():
    Student = {}
    n = int(input("Enter the number of students: "))

for i in range(n):
	name = input("NAME: ")
	age = int(input("AGE: "))
	grade = input("GRADE: ")
	Student[name] = age, grade


sorted_asc_keys = sort_dict_by_keys(Student)

sorted_desc_keys = sort_dict_by_keys(Student, reverse=True)

sorted_asc_values = sort_dict_by_values(Student)

sorted_desc_values = sort_dict_by_values(Student, reverse=True)

print("\nOriginal Student Dictionary:", Student)
print("\nAscending Order by Names:", sorted_asc_keys)
print("Descending Order by Names:", sorted_desc_keys)
print("\nAscending Order by Age and Grade:", sorted_asc_values)
print("Descending Order by Age and Grade:", sorted_desc_values)

