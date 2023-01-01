
def get_grade(s1, s2, s3):

    letter_grade=""

    # Get the average of the 3 scores
    grade_ave=float((s1+s2+s3)/3)

    # match the average to the correct letter grade
    if 90.0<=grade_ave<=100.0:
        letter_grade = "A"

    elif 80.0<=grade_ave<90.0:
        letter_grade="B"

    elif 70.0<=grade_ave<80.0:
        letter_grade="C"
    
    elif 60.0<=grade_ave<70.0:
        letter_grade="D"

    elif 0.0<=grade_ave<60.0:
        letter_grade="F"

    # return that letter grade
    return letter_grade

test_lettergrade=get_grade(95,90,93)
print(test_lettergrade)