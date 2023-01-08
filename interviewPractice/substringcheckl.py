def solution(text, ending):
    return True if (ending in text and text[-1]==ending[-1]) else False

# Can also use a python specific method .endswith

# Tests
print(solution("abc", "bc")) # >>> True
print(solution("abc", "d")) # >>> False
print(solution("samurai", "ra")) # >>> False