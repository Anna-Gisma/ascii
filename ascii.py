def PrintingCosts(Line):
    mass = []
    a = []
    k = 0
    c = 0
    for i in range(32):
        if i == 0:
            a = [' ']
        elif i == 3:
            a = ['\'', '`']
        elif i == 4:
            a = ['.']
        elif i == 6:
            a = ['"']
        elif i == 7:
            a = [',', '-', '^']
        elif i == 8:
            a = [':', '_']
        elif i == 9:
            a = ['!', '~']
        elif i == 10:
            a = ['\ ', '/', '<', '>']
        elif i == 11:
            a = [';']
        elif i == 12:
            a = ['(', ')', '|']
        elif i == 13:
            a = ['v', 'r', 'x', '+']
        elif i == 14:
            a = ['Y', '=']
        elif i == 15:
            a = ['?', 'i']
        elif i == 16:
            a = ['L', 'T', 'l', '7']
        elif i == 17:
            a = ['t', 'c', 'u', '*']
        elif i == 18:
            a = ['J', 'n', ']', '{', 'X', '}', 'f', 'I', '[']
        elif i == 19:
            a = ['V', 'w', '1', 'z']
        elif i == 20:
            a = ['o', 'j', 'C', 'F']
        elif i == 21:
            a = ['h', 'K', '4', 'k', 's']
        elif i == 22:
            a = ['2', '0', 'Z', '%', 'm']
        elif i == 23:
            a = ['8', 'P', '3', 'e', 'U', 'a']
        elif i == 24:
            a = ['&', '#', 'y', 'A']
        elif i == 25:
            a = ['b', 'd', 'P', 'G', 'S', 'q', 'H', 'N']
        elif i == 26:
            a = ['9', 'W', 'O', 'D', 'E', '6']
        elif i == 27:
            a = ['5']
        elif i == 28:
            a = ['R', 'M']
        elif i == 29:
            a = ['$', 'B']
        elif i == 30:
            a = ['g']
        elif i == 31:
            a = ['Q']
        elif i == 32:
            a = ['@']
        
        else:
            a = []
    
        mass.append(a)

    for el in Line:
        for a in mass:
            if el in a:
                k += mass.index(a)
            else:
                c += 1
        if c == 32:
            k += 23
        
            
    return k            





