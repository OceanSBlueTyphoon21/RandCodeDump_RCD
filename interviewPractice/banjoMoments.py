
# Banjo Function
def are_you_playing_banjo(name):
    name_start = name[0]
    if name_start == "R" or name_start == "r":
        name = name + " plays banjo"
    else:
        name = name + " does not playing the banjo"

    return name


test_name = "martin"

print(are_you_playing_banjo(test_name))