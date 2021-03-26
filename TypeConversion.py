def Convert_Type(value):
    try:
        return int(value)
    except TypeError:
        return str(value)


val = Convert_Type(43)
val2 = Convert_Type('string')