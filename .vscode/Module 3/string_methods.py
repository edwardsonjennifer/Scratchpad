if __name__ == "__main__":

    # Still immutable even after method

    # jar_jar = "Jar Jar Binks"
    # print(jar_jar.lower())
    # print(jar_jar.upper())

    # test_string = "This is a really long string, probably from a very long file and represents a line."
    # print('really' in test_string.lower())

    # .strip takes out the white space of the string, lstrip takes out just the left, rstrip take out just the right white space

    # .find finds the

    # Vaders_Cry = "       NOOOOOOO OOOOOOOO OOOOOOOO OOOOOOO!!!!!!!!        "
    # print("'" + Vaders_Cry + "'")
    # print("'" + Vaders_Cry.strip() + "'")

    # who_talks = "Who talk first? You talk first? I talk first."
    # talk_location = who_talks.find('talk')
    # print(talk_location)
    # print(who_talks[talk_location + len('talk'):])

    # talk_location = who_talks.find('talk', talk_location + 1)
    # print(talk_location)

    # talk_location = who_talks.find('talk', talk_location + 1)
    # print(talk_location)

    # function execute and then reassignment happens
    # .replace replaces one string for another string, but finds all intances of that string

    # sith_lords = 'Sidius, Duku'
    # sith_lords = sith_lords.replace('Duku', 'Vader')
    # print(sith_lords)

    troubled_anakin = "Not just the men, but the women and children too!"
    print(troubled_anakin.replace('women', '').replace('men', '').replace('children', ''))
