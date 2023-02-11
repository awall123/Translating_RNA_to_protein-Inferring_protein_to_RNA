rna = input("Enter RNA sequence:\n")

splitted_rna = []



while rna:

    splitted_rna.append(rna[:3])

    rna = rna[3:]



for codon in splitted_rna:

    if codon == 'AUG':

        print('M', end="")

    elif codon == 'UUU' or codon == 'UUC':
        print('F', end="")
    elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
        print('L', end="")
    elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
        print('S', end="")
    elif codon == 'UAU' or codon == 'UAC':
        print('Y', end="")
    elif codon == 'UGU' or codon == 'UGC':
        print('C', end="")
    elif codon == 'UGG':
        print('W', end="")
    elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
        print('P', end="")
    elif codon == 'CAU' or codon == 'CAC':
        print('H', end="")
    elif codon == 'CAA' or codon == 'CAG':
        print('Q', end="")
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG':
        print('R', end="")
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
        print('I', end="")
    elif codon == 'AUG':
        print('M', end="")
    elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
        print ('T', end="")
    elif codon == 'AAU' or codon == 'AAC':
        print ('N', end="")
    elif codon == 'AAA' or codon == 'AAG':
        print ('K', end="")
    elif codon == 'AGA' or codon == 'AGG':
        print ('R', end="")
    elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
        print ('V', end="")
    elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
        print ('A', end="")
    elif codon == 'GAU' or codon == 'GAC':
        print ('D', end="")
    elif codon == 'GAA' or codon == 'GAG':
        print ('E', end="")
    elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
        print ('G', end="")

print('\n')
