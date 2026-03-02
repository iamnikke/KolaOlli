
def calculate_fines(capacity, load):
    #lasketaan ylilasti
    overload = load - capacity
    #jos ylilastia on enemmän kuin kapasiteettia, törkeä sakko
    if overload > capacity:
        fines = (load - capacity) * 10

        #muuten normisakko
    else:
        fines = (load - capacity) * 5
    # palauta sakon määrä
    return fines

