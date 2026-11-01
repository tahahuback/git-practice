def student_search(student_name):
    if not student_name or not student_name.strip() :
        return " name cannot be empty "
    return f"searching for student : {student_name}"