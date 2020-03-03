f = open("./inputFile.txt")
passFile = open("passFile.txt", "w")
failFile = open("failFile.txt", "w")

# create a file with info of only people who passed
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    if line_split[2] == "F":
        failFile.write(line)
    
f.close()
passFile.close()
failFile.close()
