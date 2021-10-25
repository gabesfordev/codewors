def to_jaden_case(string):
    lst = string.split(' ')
    final_lst = []

    for word in lst:
        word = word.split(' ')
        for first_letter in word:
            remaining_letters = first_letter[1:]
            first_letter = first_letter[0].upper()
            final_lst.append(first_letter + remaining_letters)
    return ' '.join(final_lst)

string = "How can mirrors be real if our eyes aren't real"
to_jaden_case(string)