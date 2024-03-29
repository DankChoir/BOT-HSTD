###############################ALPHABET#######################################

line_0 = r'░█████╗░██████╗░░█████╗░██████╗░███████╗███████╗░██████╗░██╗░░██╗██╗░░░░░██╗██╗░░██╗██╗░░░░░███╗░░░███╗███╗░░██╗░█████╗░██████╗░░██████╗░██████╗░░██████╗████████╗██╗░░░██╗██╗░░░██╗░██╗░░░░░░░██╗██╗░░██╗██╗░░░██╗███████╗'
line_1 = r'██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝░██║░░██║██║░░░░░██║██║░██╔╝██║░░░░░████╗░████║████╗░██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝██║░░░██║██║░░░██║░██║░░██╗░░██║╚██╗██╔╝╚██╗░██╔╝╚════██║'
line_2 = r'███████║██████╦╝██║░░╚═╝██║░░██║█████╗░░█████╗░░██║░░██╗░███████║██║░░░░░██║█████═╝░██║░░░░░██╔████╔██║██╔██╗██║██║░░██║██████╔╝██║██╗██║██████╔╝╚█████╗░░░░██║░░░██║░░░██║╚██╗░██╔╝░╚██╗████╗██╔╝░╚███╔╝░░╚████╔╝░░░███╔═╝'
line_3 = r'██╔══██║██╔══██╗██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██║░░╚██╗██╔══██║██║██╗░░██║██╔═██╗░██║░░░░░██║╚██╔╝██║██║╚████║██║░░██║██╔═══╝░╚██████╔╝██╔══██╗░╚═══██╗░░░██║░░░██║░░░██║░╚████╔╝░░░████╔═████║░░██╔██╗░░░╚██╔╝░░██╔══╝░░'
line_4 = r'██║░░██║██████╦╝╚█████╔╝██████╔╝███████╗██║░░░░░╚██████╔╝██║░░██║██║╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║██║░╚███║╚█████╔╝██║░░░░░░╚═██╔═╝░██║░░██║██████╔╝░░░██║░░░╚██████╔╝░░╚██╔╝░░░░╚██╔╝░╚██╔╝░██╔╝╚██╗░░░██║░░░███████╗'
line_5 = r'╚═╝░░╚═╝╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝'

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

line_array = [line_0,line_1,line_2,line_3,line_4,line_5]

blacklist = [6,8,12,13,16,19,20,21,22,24]
 
def pos_si_tion(a):
  ##widhtidentify
  width = int()
  pos = int()
  try:
    b = blacklist.index(a)
  except ValueError:
    width = 8
  else:
    if(a==6 or a==13 or a == 16 or a==19 or a==20 or a == 21 or a ==24):
      width = 9
    elif(a==8):
      width = 3
    elif(a ==12):
      width = 11
    elif(a == 22):
      width = 14
  
  if(a<=6):
    pos = 8*a 
  elif(a>6 and a <=8):
    pos = 8*a + 1
  elif(a>8 and a<=12):
    pos = 8*a - 4
  elif(a==13):
    pos = 8*a - 1
  elif(a>13 and a <=16):
    pos = 8*a
  elif(a>16 and a<=19):
    pos = 8*a +1
  elif(a==20):
    pos = 8*a+2
  elif(a==21):
    pos = 8*a+3
  elif(a==22):
    pos = 8*a + 4
  elif(a==23 or a ==24):
    pos = 8*a + 10
  elif(a==25):
    pos = 8*a +11

  return(pos,width)

def chucai(Text):
  whole_line = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
  for dongtext in line_array:
    for word in Text:
      try:
        index = alphabet.index(word.upper())
        contemp = dongtext[(pos_si_tion(index)[0]):(pos_si_tion(index)[0]+pos_si_tion(index)[1])]
        whole_line += contemp 
      except:
        whole_line += '    '
    whole_line += '\n'
  return whole_line





###############################ALPHABET#######################################