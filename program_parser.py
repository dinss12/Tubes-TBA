#Muh Akib A Yani(1301194233)
#Maswan Pratama Putra(1301194016)
#Dinda A Wulandari(1301190156)

import string
jalan = 'jalan'
while jalan != 'berhenti':
  print('**********************************')
  print(' Selamat Datang di Program Parser')
  print('**********************************')
  print('1. Cek Kalimat')
  print('2. Keluar')
  angka = input('Masukkan angka: ')

  if angka == '1':
    #input example
    contoh = input('Masukkan kalimat: ')
    sentence = contoh
    tokens = sentence.lower().split()
    tokens.append('EOS')

    #symbols definition
    non_terminals = ['S','NN','VB']
    terminals = ['padre','madre','fratello','cugino','pane','pizza',
    'spaghetti','rendere','vendere','acquistare','consumare']

    #parser table definiton
    parser_table = {}

    parser_table[('S','padre')] = ['NN','VB','NN']
    parser_table[('S','madre')] = ['NN','VB','NN']
    parser_table[('S','fratello')] = ['NN','VB','NN']
    parser_table[('S','cugino')] = ['NN','VB','NN']
    parser_table[('S','pane')] = ['NN','VB','NN']
    parser_table[('S','pizza')] = ['NN','VB','NN']
    parser_table[('S','spaghetti')] = ['NN','VB','NN']
    parser_table[('S','rendere')] = ['error']
    parser_table[('S','vendere')] = ['error']
    parser_table[('S','acquistare')] = ['error']
    parser_table[('S','consumare')] = ['error']
    parser_table[('S','EOS')] = ['error']
    
    parser_table[('NN','padre')] = ['padre']
    parser_table[('NN','madre')] = ['madre']
    parser_table[('NN','fratello')] = ['fratello']
    parser_table[('NN','cugino')] = ['cugino']
    parser_table[('NN','pane')] = ['pane']
    parser_table[('NN','pizza')] = ['pizza']
    parser_table[('NN','spaghetti')] = ['spaghetti']
    parser_table[('NN','rendere')] = ['error']
    parser_table[('NN','vendere')] = ['error']
    parser_table[('NN','acquistare')] = ['error']
    parser_table[('NN','consumare')] = ['error']
    parser_table[('NN','EOS')] = ['error']
    
    parser_table[('VB','padre')] = ['error']
    parser_table[('VB','madre')] = ['error']
    parser_table[('VB','fratello')] = ['error']
    parser_table[('VB','cugino')] = ['error']
    parser_table[('VB','pane')] = ['error']
    parser_table[('VB','pizza')] = ['error']
    parser_table[('VB','spaghetti')] = ['error']
    parser_table[('VB','rendere')] = ['rendere']
    parser_table[('VB','vendere')] = ['vendere']
    parser_table[('VB','acquistare')] = ['acquistare']
    parser_table[('VB','consumare')] = ['consumare']
    parser_table[('VB','EOS')] = ['error']

    #stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    #input raeding initialization
    idx_token = 0
    symbol = tokens[idx_token]

    #parsing process
    while (len(stack)>0):
      top = stack[len(stack)-1]
      print('top = ',top)
      print('symbol = ',symbol)
      if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
          stack.pop()
          idx_token = idx_token+1
          symbol = tokens[idx_token]
          if symbol == 'EOS':
            print('isi stack: ',stack)
            stack.pop()
        else:
          print('error')
          break;
      elif top in non_terminals:
        print('top adalah simbol non_terminal')
        if parser_table[(top, symbol)][0] != 'error':
          stack.pop()
          symbol_to_be_pushed = parser_table[(top, symbol)]
          for i in range(len(symbol_to_be_pushed)-1,-1,-1):
            stack.append(symbol_to_be_pushed[i])
        else:
          print('error')
          break;
      else:
        print('error')
        break;
      print('isi stack: ',stack)
      print()

    #conclusion
    print()
    if symbol=='EOS' and len(stack)==0:
      print('Input string ',sentence,' diterima, sesuai Grammar')
    else:
      print('Error, input string: ',sentence,' tidak diterima, tidak sesuai Grammar')

  elif angka == '2':
    jalan = 'berhenti'