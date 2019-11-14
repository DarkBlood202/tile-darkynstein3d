def remap(value,left_min,left_max,right_min,right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min

    value_scaled = (value - left_min)/left_span

    return right_min + (value_scaled*right_span)