import time
import os
import random
import sys

add_space = 0 #Loops the removing tube
v = 20 #Splits up the tube
j = 25 #Reduces spaces to the
p = 0 #Loops to reduce the charecters
o = 1 #Loops to reduce the tube
r = 0 #reduce the tube

words = """\n\n ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ██      ██  ██████ ██   ██ ███████ ██████  
██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██ 
██      ██    ██ ██    ██ █████   ██ █████       ██      ██      ██ ██      █████   █████   ██████  
██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██ 
 ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ███████ ██  ██████ ██   ██ ███████ ██   ██ """
for char in words:
    time.sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()

words = """\n
|█████████████████████████████████████████████████████████████████████████████████████████████████|\n"""
for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

words = """
                    █   █▀█ ▄▀█ █▀▄ █ █▄ █ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀
                    █▄▄ █▄█ █▀█ █▄▀ █ █ ▀█ █▄█   █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄"""
for char in words:
    time.sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()



i1 = " ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ██      ██  ██████ ██   ██ ███████ ██████"
i2 = "██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██"
i3 = "██      ██    ██ ██    ██ █████   ██ █████       ██      ██      ██ ██      █████   █████   ██████"
i4 = "██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██"
i5 = " ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ███████ ██  ██████ ██   ██ ███████ ██   ██"

i6 = "|█████████████████████████████████████████████████████████████████████████████████████████████████|"

i7 = "                  █   █▀█ ▄▀█ █▀▄ █ █▄ █ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀"
i8 = "                  █▄▄ █▄█ █▀█ █▄▀ █ █ ▀█ █▄█   █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄"

while add_space <= 25:
  print("\n")
  print(" "*add_space+i1)
  s1 = (" "*add_space+i1)

  print(" "*add_space+i2)
  s2 = (" "*add_space+i2)

  print(" "*add_space+i3)
  s3 = (" "*add_space+i3)

  print(" "*add_space+i4)
  s4 = (" "*add_space+i4)

  print(" "*add_space+i5)
  s5 = (" "*add_space+i5)

  print("")

  print(" "*add_space+i6)
  s6 = (" "*add_space+i6)

  print("")

  print(" "*add_space+i7)
  s7 = (" "*add_space+i7)

  print(" "*add_space+i8)
  s8 = (" "*add_space+i8)

  time.sleep(0.11)
  print("\033[H\033[J")
  add_space = add_space + 1

print("\n")
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print("")
print(s6)
print("")
print(s7)
print(s8)

time.sleep(1)

print("\033[H\033[J")
while p < 20:
  l1 = '             ███████'

  l2 = '             █▓▓▓▓▓█'

  l3 = '██████████████▓▓▓▓▓█'

  l4 = '▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█'

  l5 = '░░░░░░░░░░░░░█░░░░░█'

  l6 = '░░░░░░░░░░░░░█░░░░░█'

  l7 = '             █     █'

  l8 = '             █     █'
  
  l9 = '░░░░░░░░░░░░░█░░░░░█'

  l10 = '░░░░░░░░░░░░░█░░░░░█'

  l11 = '▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█'

  l12 = '██████████████▓▓▓▓▓█'

  l13 = '             █▓▓▓▓▓█'

  l14 = '             ███████'

  a1, l1 = l1[:v], l1[v:]

  a2, l2 = l2[:v], l2[v:]
  
  a, l3 = l3[:v], l3[v:]

  b, l4 = l4[:v], l4[v:]

  c, l5 = l5[:v], l5[v:]

  d, l6 = l6[:v], l6[v:]

  e, l7 = l7[:v], l7[v:]

  f, l8 = l8[:v], l8[v:]

  g, l9 = l9[:v], l9[v:]

  h, l10 = l10[:v], l10[v:]

  i, l11 = l11[:v], l11[v:]

  k, l12 = l12[:v], l12[v:]

  l, l13 = l13[:v], l13[v:]

  m, l14 = l14[:v], l14[v:]

  print(l1+" "*j)
  print(l2+" "*j)
  print(l3+" "*j+i1)
  print(l4+" "*j+i2)
  print(l5+" "*j+i3)
  print(l6+" "*j+i4)
  print(l7+" "*j+i5)
  print(l8+" "*j)
  print(l9+" "*j+i6)
  print(l10+" "*j)
  print(l11+" "*j+i7)
  print(l12+" "*j+i8)
  print(l13+" "*j)
  print(l14+" "*j)

  p = p + 1
  v = v - 1
  j = j - 1
  time.sleep(0.11)
  print("\033[H\033[J")

print(l1+" "*j)
print(l2+" "*j)
print(l3+" "*j+i1)
print(l4+" "*j+i2)
print(l5+" "*j+i3)
print(l6+" "*j+i4)
print(l7+" "*j+i5)
print(l8+" "*j)
print(l9+" "*j+i6)
print(l10+" "*j)
print(l11+" "*j+i7)
print(l12+" "*j+i8)
print(l13+" "*j)
print(l14+" "*j)
     
b1 = '             ███████'

b2 = '             █▓▓▓▓▓█'

b3 = '██████████████▓▓▓▓▓█'

b4 = '▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█'

b5 = '░░░░░░░░░░░░░█░░░░░█'

b6 = '░░░░░░░░░░░░░█░░░░░█'

b7 = '             █     █'

b8 = '             █     █'

b9 = '░░░░░░░░░░░░░█░░░░░█'

b10 = '░░░░░░░░░░░░░█░░░░░█'

b11 = '▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█'

b12 = '██████████████▓▓▓▓▓█'

b13 = '             █▓▓▓▓▓█'

b14 = '             ███████'




x1 = "      ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ██      ██  ██████ ██   ██ ███████ ██████"
x2 = "     ██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██"
x3 = "     ██      ██    ██ ██    ██ █████   ██ █████       ██      ██      ██ ██      █████   █████   ██████"
x4 = "     ██      ██    ██ ██    ██ ██  ██  ██ ██          ██      ██      ██ ██      ██  ██  ██      ██   ██"
x5 = "      ██████  ██████   ██████  ██   ██ ██ ███████      ██████ ███████ ██  ██████ ██   ██ ███████ ██   ██"

x6 = "     |█████████████████████████████████████████████████████████████████████████████████████████████████|"

x7 = "                       █   █▀█ ▄▀█ █▀▄ █ █▄ █ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀"
x8 = "                       █▄▄ █▄█ █▀█ █▄▀ █ █ ▀█ █▄█   █▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄"

time.sleep(0.5)
print("\033[H\033[J")
while o <35:
  aa, x1 = x1[:random.randint(3,5)], x1[random.randint(3,5):]
  bb, x2 = x2[:random.randint(3,5)], x2[random.randint(3,5):]
  cc, x3 = x3[:random.randint(3,5)], x3[random.randint(3,5):]
  dd, x4 = x4[:random.randint(3,5)], x4[random.randint(3,5):]
  ee, x5 = x5[:random.randint(3,5)], x5[random.randint(3,5):]
  ff, x6 = x6[:random.randint(3,5)], x6[random.randint(3,5):]
  gg, x7 = x7[:random.randint(3,5)], x7[random.randint(3,5):]
  hh, x8 = x8[:random.randint(3,5)], x8[random.randint(3,5):]

  print(b1)
  print(b2)
  print(b3+x1)
  print(b4+x2)
  print(b5+x3)
  print(b6+x4)
  print(b7+x5)
  print(b8)
  print(b9+x6)
  print(b10)
  print(b11+x7)
  print(b12+x8)
  print(b13)
  print(b14)

  o = o + 1
  time.sleep(0.1)
  print("\033[H\033[J")

print("\033[H\033[J")
while r < 21:
  aa1, b1 = b1[:r], b1[r:]
  aa2, b2 = b2[:r], b2[r:]
  aa3, b3 = b3[:r], b3[r:]
  aa4, b4 = b4[:r], b4[r:]
  aa5, b5 = b5[:r], b5[r:]
  aa6, b6 = b6[:r], b6[r:]
  aa7, b7 = b7[:r], b7[r:]
  aa8, b8 = b8[:r], b8[r:]
  aa9, b9 = b9[:r], b9[r:]
  aa10, b10 = b10[:r], b10[r:]
  aa11, b11 = b11[:r], b11[r:]
  aa12, b12 = b12[:r], b12[r:]
  aa13, b13 = b13[:r], b13[r:]
  aa14, b14 = b14[:r], b14[r:]
  print(b1+"\n"+b2+"\n"+b3+"\n"+b4+"\n"+b5+"\n"+b6+"\n"+b7+"\n"+b8+"\n"+b9+"\n"+b10+"\n"+b11+"\n"+b12+"\n"+b13+"\n"+b14)
  r = r + 1
  time.sleep(0.15)
  print("\033[H\033[J")
print("\033[H\033[J")
