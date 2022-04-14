def remove_vowels(namen_lijst):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    namen_lijst_filtered = []

    # remove vowels from names in list
    for naam in namen_lijst:
        for letter in naam:
            if letter in vowels:
                naam = naam.replace(letter, '')
        namen_lijst_filtered.append(naam)


    # create variable for number of names
    aantal_namen = len(namen_lijst)
    return namen_lijst_filtered, aantal_namen