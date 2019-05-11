# Define function for user input
def filein(defa='undefined'):
    i = None
    while i is None:
        try:
            i = open(input('Enter file name: '))
        except:
            try:
                i = open(defa)
            except:
                print ('Invalid file name, try again')
                continue
    return i


# Open file and create dictionary
file = filein()
answer = {}

# Split lines in file to isolate times and populate to dictionary
for line in file:
    if not line.startswith('From '): continue
    time = line.split()[5].split(':')[0]
    answer[time] = answer.get(time, 0) +1

# Print dictionary 1 result per line
for k,v in sorted(answer.items()):
    print (k,v)
