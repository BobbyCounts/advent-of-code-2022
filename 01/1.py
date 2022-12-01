with open("input.txt", "r") as input_file:
    #data list for each elf
    elf_calories = [0]
    #read file line by line
    for line in input_file:
        if(line == '\n'):
            elf_calories.append(0)
        else:
            elf_calories[-1] += int(line)
        
    #get the biggest  
    elf_calories.sort(reverse=True)
    print(f"Max Value: {elf_calories[0]}")
    print(f"Max 3: {elf_calories[0] + elf_calories[1] + elf_calories[2]}")
