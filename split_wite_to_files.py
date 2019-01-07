man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)

        except ValueError:
            pass

    data.close()

except IOError:
    print("The data file is missing")

try:
    out1 = open("man.txt", "w")
    out2 = open("other.txt", 'w')

    print(man, file = out1)
    print(other, file = out2)

    
except IOError:
    print("unable to create file")

finally:
    out1.close()
    out2.close()
    
