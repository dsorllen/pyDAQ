#

def temp_2_float(value_str):
    dec = float(value_str.split('E')[1])
    value = float(value_str.split('E')[0]) * 10 ** (dec)
    return round(value, 2)