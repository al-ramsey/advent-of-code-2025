#file = r"[PATH]"
#filein = open(file, "r", encoding='UTF-8')
#lines = filein.readlines()
#filein.close()
#line = lines[0]

def part1(line):

    ranges = line.split(",")
    ranges = [r.split("-") for r in ranges]
    count = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1])+1):
            # cut the string in two
            if len(str(i)) % 2 == 0:
                # check if the two terms are equal
                if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                    count += i
        
    return count

#print(part1(line))

def periodic(n : str):
    # check if a string is periodic
    for i in range(2, len(n)+1):
        if len(n) % i == 0:
            k = int(len(n)/i)
            pieces = [n[k*j:k*j+k] for j in range(int((len(n)-k)/k)+1)]
            if len(set(pieces)) == 1:
                return True
            
    return False

def part2(line):
    
    ranges = line.split(",")
    ranges = [r.split("-") for r in ranges]
    count = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1])+1):
            if periodic(str(i)):
                count += i
        
    return count

#print(part2(line))