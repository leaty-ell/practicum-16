def common_courses(students_courses) -> int:
    """
    Determines how many courses all students have chosen.
    
    Args:
        students_courses (list): List of lists, containing courses for one student
    
    Returns:
        int: Number of courses chosen by all students
    """
    if not students_courses:
        return 0
    
    sets = []
    for courses in students_courses:
        sets.append(set(courses))
    
    common = sets[0]
    for s in sets[1:]:
        common = common.intersection(s)
    return len(common)

def main():
    """
    Main function to read input and display result
    """
    n = int(input())
    students_courses = []
    for i in range(n):
        courses = input().split()
        students_courses.append(courses)
    
    result = common_courses(students_courses)
    print(result)

if __name__ == "__main__":
    main()
