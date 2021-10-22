def is_isogram(string):

    unique_list = []

    for letter in string.lower():

        if letter not in unique_list:
            unique_list.append(letter)

    if len(unique_list) == len(string):
        return True
    return False