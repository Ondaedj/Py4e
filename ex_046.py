# Define function to compute pay
def computepay(h, r):
    if h > 40: ot = h - 40
    else: ot = 0
    pay = h * r + ot * r * 0.5
    return pay


# Define another function to ensure proper input
def posfloat(inp):
    i = None
    while i is None:
        try: i = float (input (inp))
        except: print(inp, 'must be an integer'); continue
        if i <= 0: i = None; print(inp, 'must b greater than 0'); continue
    return i


# Receive hour and rate information
hrs = posfloat('Hours')
rate = posfloat('Rate')

# Print result
print (computepay (hrs, rate))
