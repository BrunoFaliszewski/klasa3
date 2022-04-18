with open('dane_6_1.txt', 'r') as file:
    words = file.readlines()
    newwords = []

    for i in range(len(words)):
        words[i] = words[i].replace('\n', '')
    
    for word in words:
        newword = ''
        for i in range(len(word)):
            if ord(word[i]) + (107%26) > 90:
                newword += chr(ord(word[i]) + (107%26) - 26)
            else:
                newword += chr(ord(word[i]) + (107%26))
        newwords.append(newword)

with open('wyniki_6_1.txt', 'w') as file:
    text = ''
    for word in newwords:
        word += '\n'
        text += word
    
    file.write(text)

with open('dane_6_2.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    
    dict = {}

    for line in lines:
        splitted = line.split()
        if len(splitted) == 2:
            dict[splitted[0]] = int(splitted[1])
        else:
            dict[splitted[0]] = 0
    
    newwords = []

    for key in dict:
        value = dict[key]
        newword = ''
        for i in range(len(key)):
            if ord(key[i]) - (value%26) < 65:
                newword += chr(ord(key[i]) - (value%26) + 26)
            else:
                newword += chr(ord(key[i]) - (value%26))
        
        newwords.append(newword)
    
with open('wyniki_6_2.txt', 'w') as file:
    text = ''
    for word in newwords:
        word += '\n'
        text += word
    
    file.write(text)

def isCrypted(str1, str2):
    if ord(str2[0]) > ord(str1[0]):
        k = ord(str2[0]) - ord(str1[0])
    else:
        k = ord(str2[0]) - ord(str1[0]) + 26
    for i in range(len(str1)):
        if ord(str1[i]) + k > 90:
            if ord(str1[i]) + k - 26 == ord(str2[i]):
                pass
            else:
                return False
            pass
        else:
            if ord(str1[i]) + k == ord(str2[i]):
                pass
            else:
                return False
            pass
    
    return True

with open('dane_6_3.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    
    dict = {}

    for line in lines:
        splitted = line.split()
        dict[splitted[0]] = splitted[1]
    
    newwords = []

    for key in dict:
        value = dict[key]

        if not isCrypted(key, value):
            newwords.append(key)
    
with open('wyniki_6_3.txt', 'w') as file:
    text = ''
    for word in newwords:
        word += '\n'
        text += word
    
    file.write(text)