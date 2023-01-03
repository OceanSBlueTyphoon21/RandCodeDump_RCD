def bool_to_word(boolean):
    match boolean:
        case True:
            return "Yes"

        case False:
            return "No"

        case _:
            return "You have not entered a bool value"

#test of bool2word function
print(bool_to_word(True))
print(bool_to_word(False))