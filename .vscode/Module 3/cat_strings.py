if __name__ == "__main__":

    #Concatenation

    #You can concatenate two strings together using +

    # leia = "I love you."
    # han = "I know."

    # print(leia +' ' + han)

    # Indexing a letter, Slice (ex.0:9, starts at 0, slices TO the end index(not including the index))
    # Shortcut: [:9] is [0:9] & [10:15] is [10:]assumes beginning of string or end of string
    
    # ship = "Mellinium Falcon"
    # print(ship[0:9])
    
    # bold_statement = ship + " is the fastest in the galaxy."
    # print(bold_statement)

    # Value cannot be changed or imutable, unless it is reassigned

    # ship = 'S' + ship[1:]
    # print(ship)

    # in - If the right side contains the value of the left side

    jedi_masters = "Obi-Wan Kenobi, Yoda, Qui-Gon Gin"
    print('Anakin' in jedi_masters)

    council_members = "Anakin, Obi-Wan Kenobi, Yoda, Qui-Gon Gin"
    print('Anakin' in council_members)