#
#
def old_units_in_mm(p_old_unit_string):
    ##
    ##
    ##

    # Hand is 101.6mm
    if p_old_unit_string.lower() == "hand":
        ret_val = 101.6
    # Metric foot is 300mmm
    elif p_old_unit_string.lower() == "metric foot":
        ret_val = 300
    # Horse is 2400mmm
    elif p_old_unit_string.lower() == "horse":
        ret_val = 2400
    else:
        ret_val = 0

    return ret_val


def convert_old_unit_to_mmm(p_value, p_unit):
    ##
    ##

    unit_value = old_units_in_mm(p_unit)
    ret_values = unit_value * p_value
    ret_val = str(ret_values)
    pe_val = str(p_value)

    return (pe_val + " " + p_unit + "s" + " equals: " + ret_val+ " mm")

print(convert_old_unit_to_mmm(4, "hand"))
