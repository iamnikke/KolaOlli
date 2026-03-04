def multiply_load(distance, load):
    multiplier = distance / 1000 + 1
    loadValue = load * multiplier * 3
    return loadValue

