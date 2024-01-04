#Muh Akib A Yani(1301194233)
#Maswan Pratama Putra(1301194016)
#Dinda A Wulandari(1301190156)

import string
jalan = 'jalan'
while jalan != 'berhenti':
  print('********************************************')
  print(' Selamat Datang di Program Lexical Analyzer')
  print('********************************************')
  print('1. Cek Kata')
  print('2. Keluar')
  angka = input('Masukkan angka: ')

  if angka == '1';
    #input example
    contoh = input('Masukkan string yang ingin diperiksa: ')
    sentence = contoh
    input_string = sentence.lower()+'#'

    #initialization
    alphabet_list = list(string.ascii_lowercase)
     state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 
     'q24', 'q25', 'q26', 'q27', 'q28', 'q29','q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 
     'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 
     'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62', 'q63', 'q64']

   transition_table = {}

    for state in state_list:
      for alphabet in alphabet_list:
       transition_table[(state, alphabet)] = 'error'
      transition_table[(state, '#')] = 'error'
      transition_table[(state, ' ')] = 'error'

    #spacing string
    transition_table['q0', ' '] = 'q0'
    transition_table['q13', ' '] = 'q14'
    transition_table['q5', ' '] = 'q14'
    transition_table['q20', ' '] = 'q14'
    transition_table['q29', ' '] = 'q14'
    transition_table['q37', ' '] = 'q14'
    transition_table['q45', ' '] = 'q14'
    transition_table['q49', ' '] = 'q14'
    transition_table['q54', ' '] = 'q14'
    transition_table['q64', ' '] = 'q14'

    #transition table for following token
    transition_table['q0', 'p'] = 'q1'
    transition_table['q1', 'a'] = 'q2'
    transition_table['q2', 'd'] = 'q3'
    transition_table['q3', 'r'] = 'q4'
    transition_table['q4', 'e'] = 'q5'
    transition_table['q0', 'm'] = 'q1'
    transition_table['q0', 'f'] = 'q6'
    transition_table['q6', 'r'] = 'q7'
    transition_table['q7', 'a'] = 'q8'
    transition_table['q8', 't'] = 'q9'
    transition_table['q9', 'e'] = 'q10'
    transition_table['q10', 'l'] = 'q11'
    transition_table['q11', 'l'] = 'q12'
    transition_table['q12', 'o'] = 'q13'
    transition_table['q21', 'u'] = 'q16'
    transition_table['q16', 'g'] = 'q17'
    transition_table['q17', 'i'] = 'q18'
    transition_table['q18', 'n'] = 'q19'
    transition_table['q19', 'o'] = 'q20'
    transition_table['q0', 'c'] = 'q21'
    transition_table['q21', 'o'] = 'q22'
    transition_table['q22', 'n'] = 'q23'
    transition_table['q23', 's'] = 'q24'
    transition_table['q24', 'u'] = 'q25'
    transition_table['q25', 'm'] = 'q26'
    transition_table['q26', 'a'] = 'q27'
    transition_table['q27', 'r'] = 'q28'
    transition_table['q28', 'e'] = 'q29'
    transition_table['q0', 'r'] = 'q31'
    transition_table['q31', 'e'] = 'q32'
    transition_table['q32', 'n'] = 'q33'
    transition_table['q33', 'd'] = 'q34'
    transition_table['q34', 'e'] = 'q35'
    transition_table['q35', 'r'] = 'q36'
    transition_table['q36', 'e'] = 'q37'
    transition_table['q0', 'v'] = 'q31'
    transition_table['q2', 'n'] = 'q48'
    transition_table['q48', 'e'] = 'q49'
    transition_table['q1', 'i'] = 'q51'
    transition_table['q51', 'z'] = 'q52'
    transition_table['q52', 'z'] = 'q53'
    transition_table['q53', 'a'] = 'q54'
    transition_table['q0', 'a'] = 'q55'
    transition_table['q55', 'c'] = 'q56'
    transition_table['q56', 'q'] = 'q57'
    transition_table['q57', 'u'] = 'q58'
    transition_table['q58', 'i'] = 'q59'
    transition_table['q59', 's'] = 'q60'
    transition_table['q60', 't'] = 'q61'
    transition_table['q61', 'a'] = 'q62'
    transition_table['q62', 'r'] = 'q63'
    transition_table['q63', 'e'] = 'q64'

    #transition table for new token
    transition_table['q14', 'm'] = 'q1'
    transition_table['q14', 'p'] = 'q1'
    transition_table['q14', 'f'] = 'q6'
    transition_table['q14', 'c'] = 'q21'
    transition_table['q14', 'r'] = 'q31'
    transition_table['q14', 'v'] = 'q31'
    transition_table['q14', 's'] = 'q38'
    transition_table['q14', 'a'] = 'q55'

    #transition table Last
    transition_table['q5', '#'] = 'accept'
    transition_table['q13', '#'] = 'accept'
    transition_table['q20', '#'] = 'accept'
    transition_table['q14', '#'] = 'accept'
    transition_table['q20', '#'] = 'accept'
    transition_table['q29', '#'] = 'accept'
    transition_table['q37', '#'] = 'accept'
    transition_table['q45', '#'] = 'accept'
    transition_table['q49', '#'] = 'accept'
    transition_table['q54', '#'] = 'accept'
    transition_table['q64', '#'] = 'accept'

    #lexical analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
      current_char = input_string[idx_char]
      current_token += current_char
      state = transition_table[(state, current_char)]
      if state=='q5' or state=='q13' or state=='q20' or state=='q29' or state=='q37' or state=='q45' or state=='q49' or state=='q54' or state=='q64':
        print('current token: ', current_token, ', valid')
      current_token = ''
      if state =="error":
        print("error")
      break
      idx_char = idx_char + 1

    #conclusion
    if state == "accept":
      print('semua token diinput: ', sentence, ', valid')

  elif angka == '2':
    jalan = 'berhenti'