def string_to_array(s):
    match s:
        case "":
            return [""]
        case _:
            return s.split()
    
# quick test
print(string_to_array("I Love coding"))
print(string_to_array(""))