#Raval Cheruku, 1st April, is...else and while

while True:
    last_name = input("Enter student's last name (type 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
#asks for last name and quits if ZZZ is typed
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
#asks for first name in string and gpa in float
    if gpa >= 3.5:
        print("{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print("{first_name} {last_name} has made the Honor Roll.")
    else:
        print("{first_name} {last_name} does not qualify for any honors.")