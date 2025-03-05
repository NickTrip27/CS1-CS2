'''
Nicholas Triplett

Sources - https://github.com/jmelahman/python-for-everybody-solutions/blob/master/exercise10_3.py + https://github.com/jmelahman/python-for-everybody-solutions/blob/master/exercise10_2.py + https://github.com/jmelahman/python-for-everybody-solutions/blob/master/exercise10_2.py
'''
guess = input("For excersice 1, 2, or 3, enter 1, 2, or 3: ")

if guess == '1':
    dictionary_addresses = dict()          
    lst = list()

    fhand = input('Enter file name: ')
    try:
        fhand = open(fhand)
    except FileNotFoundError:
        print('File cannot be opened:', fhand)
        quit()

    for line in fhand:
        words = line.split()
        if len(words) < 2 or words[0] != 'From':
            continue
        else:
            if words[1] not in dictionary_addresses:
                dictionary_addresses[words[1]] = 1     
            else:
                dictionary_addresses[words[1]] += 1      
    for key, val in list(dictionary_addresses.items()):
        lst.append((val, key))             

    lst.sort(reverse=True)               
    for count, email in lst[:1]:          
        print(email, count)
elif guess == '2':
    dictionary_hours = dict()               # Initialize variables
    lst = list()

    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print('File cannot be opened:', fname)
        quit()

    for line in fhand:
        words = line.split()
        if len(words) < 5 or words[0] != 'From':
            continue

        col_pos = words[5].find(':')
        hour = words[5][:col_pos]
        if hour not in dictionary_hours:
            dictionary_hours[hour] = 1      # First entry
        else:
            dictionary_hours[hour] += 1     # Additional counts

    for key, val in list(dictionary_hours.items()):
        lst.append((key, val))              # Fills list with hour, count of dict

    lst.sort()                              # Sorts by hour
    for key, val in lst:
        print(key, val)
elif guess == '3':
    import string

    counts = 0                          # Initialize variables
    dictionary_counts = dict()
    relative_lst = list()

    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print('File cannot be opened:', fname)
        exit()

    for line in fhand:
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()

        # Removes numbers and punctuation then sets all letters to lower case
        words = line.split()
        for word in words:
            for letter in word:
                # Count each letter for relative frequencies
                counts += 1
                if letter not in dictionary_counts:
                    dictionary_counts[letter] = 1
                else:
                    dictionary_counts[letter] += 1

    for key, val in list(dictionary_counts.items()):
        relative_lst.append((val / counts, key))  # Computes the relative frequency

    relative_lst.sort(reverse=True)         # Sorts from highest rel freq

    for key, val in relative_lst:
        print(key, val)