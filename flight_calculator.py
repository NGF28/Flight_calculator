
def calculate_flight_time(weight_grams):  #copilot suggested edit the program because it make it more efficient and readable.
    if weight_grams < 0:                                
        raise ValueError("Weight cannot be negative.")

    result = 180 - 0.1 * weight_grams
    return result


def flight_time_table (max_weight_grams, step_grams): 
    cWeight = 0.0
    weight_flight_times = []
    while (cWeight <= max_weight_grams):
        flight_time = calculate_flight_time(cWeight)          #I rejected the copilot suggestion because it was not necessary to change the variable name from cWeight to cweight, as it is already clear and readable.
        weight_flight_times.append((cWeight, flight_time))
        cWeight = step_grams + cWeight                         #copilot suggested edit the program because it make it more efficient and readable.
        return weight_flight_times
    
