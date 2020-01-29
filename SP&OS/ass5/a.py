fptr = open('a.asm', 'r')
addressFile = open('output.txt', 'w')

prev_add = 0
len1 = 0
lit = []

statement_add = []

index_symb = 1
index_lit = 1
index_pool = 1

registers = {'AREG': 1, 'BREG': 2, 'CREG': 3, 'DREG': 4}
comp_code = {'LT': 1, 'LE': 2, 'EQ': 3, 'GT': 4, 'GE': 5, 'ANY': 6}
instru_statement = {'STOP': '00', 'ADD': '01', 'SUB': '02', 'MULT': '03', 'MOVER': '04', 'MOVEM': '05', 'COMP': '06',
                    'BC': '07', 'DIV': '08', 'READ': '09', 'PRINT': '10'}

pool_table = [['index', 'literal']]
lit_table = [['index', 'literal', 'address']]
symb = [['index', 'symbol', 'address']]
IC = [['address', 'mnemonic opcode', 'operand']]

for f in fptr:
    words = f.upper().split()
    if words[0][-1] == ':':
        symb.append([index_symb, words[0][0:-1], prev_add])
        index_symb += 1
        # print(symb)
        statement_add.append([words[0], prev_add])
        if words[1] in ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT']:

            if words[1] in ['ADD', 'SUB', 'MULT', 'DIV', 'MOVER', 'MOVEM']:
                if words[2][5] == '=' and words[2][6] == "'" and words[2][8] == "'":
                    lit.append(words[2][5:])
                    IC.append([prev_add, ('IS', instru_statement[words[1]]),
                               ((registers[words[2][0:4]]), ('L', words[2][7]))])
                else:
                    IC.append([prev_add, ('IS', instru_statement[words[1]]),
                               ((registers[words[2][0:4]]), ('S', [i[0] for i in symb if i[1] == words[2][5]]))])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
            elif words[1] == 'COMP':
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                # IC.append([prev_add, ('IS', instru_statement[words[1]]), ((registers[words[2][0:4]]), ('L', words[2][7]))])
                len1 = 1
                prev_add = prev_add + len1

            elif words[1] == 'BC':
                IC.append([prev_add, ('IS', instru_statement[words[1]]),
                           ((comp_code[words[2]]), ('S', [i[0] for i in symb if i[1] == words[3]]))])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
            elif words[1] in ['READ', 'PRINT', 'STOP']:
                if words[1] == 'STOP':
                    IC.append([prev_add, ('IS', instru_statement[words[1]])])
                else:
                    IC.append(
                        [prev_add, ('IS', instru_statement[words[1]]), ('S', [i[0] for i in symb if i[1] == words[2]])])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
        elif words[2] in ['DS', 'DC']:
            if words[2] == 'DS':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[1]]), ('DL', '02'), ('C', words[3])])
                symb.append([index_symb, words[1], prev_add])
                index_symb += 1
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = words[3]
                prev_add = prev_add + len1
            elif words[2] == 'DC':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[1]]), ('DL', '01'), ('C', words[3])])
                symb.append([index_symb, words[1], prev_add])
                index_symb += 1
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1

        elif words[1] in ['START', 'END', 'ORIGIN', 'EQU', 'LTORG']:
            if words[1] == 'START':
                IC.append([prev_add, ('AD', '01'), ('C', words[2])])
                addressFile.write(f)
                len1 = 1
                prev_add = int(words[2])
            elif words[1] == 'LTORG':
                IC.append([prev_add, ('AD', '05')])
                addressFile.write(f)
                for l in lit:
                    pool_table.append([index_pool, l])
                    lit_table.append([index_lit, l, prev_add])
                    index_lit += 1
                    len1 = 1
                    IC.append([prev_add, ('S',), ('DL', '01'), ('C', l)])
                    addressFile.write(l + ' ' + str(prev_add) + '\n')
                    prev_add += len
                lit = []
                index_pool += 1
            elif words[1] == 'END':
                IC.append(['AD', '02'])
                addressFile.write(f)
                for l in lit:
                    pool_table.append([index_pool, l])
                    lit_table.append([index_lit, l, prev_add])
                    index_lit += 1
                    len1 = 1
                    IC.append([prev_add, ('S',), ('DL', '01'), ('C', l)])
                    addressFile.write(l + ' ' + str(prev_add) + '\n')
                    prev_add += len
                index_pool += 1
            elif words[1] == 'ORIGIN':
                IC.append([prev_add, ('AD', '03'), ('S',)])
                len1 = 1
                addressFile.write(f)
                for statement, address in statement_add:
                    if statement in words[2]:
                        if '+' in words[2]:
                            a = words[2].find('+')
                            prev_add = address + int(words[2][a:])
                        if '-' in words[2]:
                            a = words[2].find('-')
                            prev_add = address - int(words[2][a:])
            elif words[2] == 'EQU':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[1]])('AD', '04')])
                addressFile.write(f)
    else:
        statement_add.append([words[0], prev_add])
        if words[0] in ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT']:

            if words[0] in ['ADD', 'SUB', 'MULT', 'DIV', 'MOVER', 'MOVEM']:
                if words[1][5] == '=' and words[1][6] == "'" and words[1][8] == "'":
                    lit.append(words[1][5:])
                    IC.append([prev_add, ('IS', instru_statement[words[0]]),
                               ((registers[words[1][0:4]]), ('L', words[1][7]))])
                else:
                    IC.append([prev_add, ('IS', instru_statement[words[0]]),
                               ((registers[words[1][0:4]]), ('S', [i[0] for i in symb if i[1] == words[1][5]]))])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
            elif words[0] == 'COMP':
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
            elif words[0] == 'BC':
                IC.append([prev_add, ('IS', instru_statement[words[0]]),
                           ((comp_code[words[1]]), ('S', [i[0] for i in symb if i[1] == words[2]]))])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
            elif words[0] in ['READ', 'PRINT', 'STOP']:
                if words[0] == 'STOP':
                    IC.append([prev_add, ('IS', instru_statement[words[0]])])
                else:
                    IC.append(
                        [prev_add, ('IS', instru_statement[words[0]]), ('S', [i[0] for i in symb if i[1] == words[1]])])
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
        elif words[0] in ['START', 'END', 'ORIGIN', 'EQU', 'LTORG']:
            if words[0] == 'START':
                IC.append([prev_add, ('AD', '01'), ('C', words[1])])
                addressFile.write(f)
                len1 = 1
                prev_add = int(words[1])
            elif words[0] == 'LTORG':
                IC.append([prev_add, ('AD', '05')])
                addressFile.write(f)
                for l in lit:
                    pool_table.append([index_pool, l])
                    lit_table.append([index_lit, l, prev_add])
                    index_lit += 1
                    len1 = 1
                    # IC.append([prev_add,])
                    IC.append([prev_add, ('S',), ('DL', '01'), ('C', l)])
                    addressFile.write(l + ' ' + str(prev_add) + '\n')
                    prev_add += len1
                index_pool += 1
                lit = []
            elif words[0] == 'END':
                IC.append(['AD', '02'])
                addressFile.write(f)
                for l in lit:
                    pool_table.append([index_pool, l])
                    lit_table.append([index_lit, l, prev_add])
                    index_lit += 1

                    len1 = 1
                    IC.append([prev_add, ('S',), ('DL', '01'), ('C', l)])
                    addressFile.write(l + ' ' + str(prev_add) + '\n')
                    prev_add += len1
                index_pool += 1
            elif words[0] == 'ORIGIN':
                IC.append([prev_add, ('AD', '03'), ('S',)])
                len1 = 1
                addressFile.write(f)
                for statement, address in statement_add:
                    if statement in words[1]:
                        if '+' in words[1]:
                            a = words[1].find('+')
                            prev_add = address + int(words[1][a:])
                        if '-' in words[1]:
                            a = words[1].find('-')
                            prev_add = address - int(words[1][a:])
            elif words[1] == 'EQU':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[0]])('AD', '04')])
                addressFile.write(f)
        elif words[1] in ['DS', 'DC']:
            if words[1] == 'DS':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[1]]), ('DL', '02'), ('C', words[2])])
                symb.append([index_symb, words[0], prev_add])
                index_symb += 1
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = words[2]
                prev_add = prev_add + len1
            elif words[1] == 'DC':
                IC.append([prev_add, ('S', [i[0] for i in symb if i[1] == words[1]]), ('DL', '01'), ('C', words[2])])
                symb.append([index_symb, words[0], prev_add])
                index_symb += 1
                addressFile.write(f[0:-1] + ' ' + str(prev_add) + '\n')
                len1 = 1
                prev_add = prev_add + len1
fptr.close()
addressFile.close()
print("literal table is:", lit_table)
print("symbol table is:", symb)
print("pool table is:", pool_table)
# print("Intermediate code is:",IC)
for i in IC:
    print(i)


