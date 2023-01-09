def past(h, m, s):
    return (h*60*60*1000) + (m*60000) + (s*1000)  # returns the amount of milliseconds

# test function:
print(past(0,1,1))