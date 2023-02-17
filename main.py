total_student = int(input("enter the total student:"))
with_maths = int(input("enter the student with maths:"))
with_bio = int(input("enter the student with bio:"))

without_maths_bio = total_student - with_maths - with_bio
with_maths_bio = with_maths + with_bio
print(f"total number of students: {total_student}")
print(f"number of students with maths:{with_maths}")
print(f"number of students with bio:{with_bio}")

print(f"number of students without maths and bio:{without_maths_bio}")
print(f"number of students with_maths and _bio:{with_maths_bio}")