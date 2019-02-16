#


# To format item in flag format
def flag_format(flag):
    string_input = str(flag)
    solution = "picoCTF{" + string_input + "}"
    print(solution)
    return solution


# To convert hex to ascii string
def hex_to_ascii(hex_code):
    return bytearray.fromhex(hex_code).decode()


# To convert decimal to binary
def deci_to_bin(deci):
    return "{0:b}".format(deci)


# To convert from Hex to decimal and returns hex code as a float
def hex_to_deci(hex_code):
    decimal_value = int(hex_code, 16)
    print(decimal_value)
    return decimal_value


if "__main__" == __name__:
    flag_format(hex_to_deci("3D"))
    flag_format(deci_to_bin(27))
    flag_format(hex_to_ascii("41"))