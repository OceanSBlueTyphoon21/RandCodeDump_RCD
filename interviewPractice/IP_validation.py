def is_valid_IP(strng):
# this function validates whether an IPv4 Address
# is valid

    octet_list = strng.split(".")
    
    #check length of IP address for 4 Octets
    if len(octet_list) != 4:
        return False

    #check octets are between 0 and 255 inclusive
    for octet in octet_list:
        #print(octet) for debugging
        if not(octet.isdigit()) or octet != str(int(octet)) or not int(octet) in range(0,256):
            return False
            break

    return True



#testing
IPaddress = "1.abc.3.4"

print(is_valid_IP(IPaddress))

