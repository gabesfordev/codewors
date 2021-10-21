def add_length(str_):
    """Returns words and length of the words"""

    return ['{} {}'.format(word, len(word)) for word in str_.split()]

