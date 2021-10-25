def DNA_strand(dna):
    symbols = []

    for symbol in dna:
        if symbol == 'A':
            symbol = 'T'
            symbols.append(symbol)
        elif symbol == 'T':
            symbol = 'A'
            symbols.append(symbol)
        elif symbol == 'C':
            symbol = 'G'
            symbols.append(symbol)
        elif symbol == 'G':
            symbol = 'C'
            symbols.append(symbol)

    return ''.join(symbols)