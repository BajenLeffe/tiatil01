def convert_temp(val, src, tgt):
    if src == 'C' and tgt == 'F':
        return (val * 9/5) + 32
    elif src == 'F' and tgt == 'C':
        return (val - 32) * 5/9
    elif src == 'C' and tgt == 'K':
        return val + 273.15
    elif src == 'K' and tgt == 'C':
        return val - 273.15
    elif src == 'F' and tgt == 'K':
        return (val - 32) * 5/9 + 273.15
    elif src == 'K' and tgt == 'F':
        return (val - 273.15) * 9/5 + 32
    else:
        return("invalid source or target unit")   
input_value = float(input("enter the temperature value: "))
input_unit = input("enter the source unit (C, F, K): ").upper()
target_unit = input("enter the target unit (C, F, K): ").upper()
result = convert_temp(input_value, input_unit, target_unit)
print(f"{input_value} {input_unit} is {result:.2f} {target_unit}")