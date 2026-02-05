students=[]
def add_student():
  name=input("Enter name: ")
  roll_no=int(input("Enter roll number: "))
  marks=float(input("Enter marks: "))
  student={"name":name,"roll_no":roll_no,"marks":marks}
  students.append(student)
  print("Student added successfully.")
def view_students():
  if not students:
    print("No students found.")
    return
  for student in students:
    print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
def search_student():
  roll_no=int(input("Enter roll number to search: "))
  for student in students:
    if student['roll_no']==roll_no:
      print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
      return
  print("Student not found.")
def delete_student():
  roll_no=int(input("Enter roll number to delete: "))
  for i, student in enumerate(students):
    if student['roll_no']==roll_no:
      del students[i]
      print("Student deleted successfully.")
      return
  print("Student not found.")
def update_student():
  roll_no=int(input("Enter roll number to update: "))
  for student in students:
    if student['roll_no']==roll_no:
      name=input("Enter new name: ")
      marks=float(input("Enter new marks: "))
      student['name']=name
      student['marks']=marks
      print("Student updated successfully.")
      return
  print("Student not found.")
def main():
  while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    choice=input("Enter your choice: ")
    if choice=='1':
      add_student()
    elif choice=='2':
      view_students()
    elif choice=='3':
      search_student()
    elif choice=='4':
      delete_student()
    elif choice=='5':
      update_student()
    elif choice=='6':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
if __name__=="__main__":
  main()
