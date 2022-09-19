def grade2GPA(grade):
    ''' Grade to GPA calculator
        Input must be between 0 and 100
        returns GPA'''

    if grade > 100 or grade < 0:
        print("Please enter a number between 0 and 100")
        return None
        
    elif grade < 60:
        return 1

    else:
        tensplace = grade//10 #this doesn't work for 100!

        gpa = tensplace - 5 # this doesn't work for numbers less than 60

        return gpa
