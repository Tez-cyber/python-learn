# ----------------------------Strings
course = "Python for beginners"
another = course[:]#------------------ To slice in a string
print(course[1:])
print(len(course))


name = 'Jeniffer'
print(name[1:-1])


# String methods
print(course.upper())
print(course.lower())
print(course.find('f'))
print(course.title())
print(course.replace('beginners', 'Absolute Beginners')) #-----Case senstive
print('Python' in course)