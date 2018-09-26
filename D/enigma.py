#Static
abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor_number_i=['EKMFLGDQVZNTOWYHXUSPAIBRCJ','Q',0,0]
rotor_number_ii=['AJDKSIRUXBLHWTMCQGZNPYFVOE','E',0,0]
rotor_number_iii=['BDFHJLCPRTXVZNYEIWGAKMUSQO','V',0,0]
rotor_number_iv=['ESOVPZJAYQUIRHXLNFTGKDCMWB','J',0,0]
rotor_number_v=['VZBRGITYUPSDNHLXAWMJQOFECK','Z',0,0]
reflector_b='YRUHQSLDPXNGOKMIEBFZCWVJAT'

#Utility functions
def rot(c, offset):
    return abc[(abc.find(c) + offset) % len(abc)]

def swap(text,plug):
    return text.translate(str.maketrans(plug, plug[::-1]))

def notch(rotor_left, rotor_right):
    return abc[(rotor_left[2]-1)%len(abc)]==rotor_left[1] or abc[(rotor_right[2])%len(abc)]==rotor_right[1]
  
def shift_rotor(rotor):
    return [rotor[0][1:]+rotor[0][0],rotor[1],(rotor[2]+1) %len(rotor[0]),rotor[3]]

def shift_rotor_n(rotor,n):
    x=rotor
    for i in range(n):
        x=shift_rotor(x)
    return x

def incr_rotors(rotors):
    incremented_rotors=rotors
    incremented_rotors[0]=shift_rotor(incremented_rotors[0])
    if(notch(incremented_rotors[0],incremented_rotors[1])):
        incremented_rotors[1]=shift_rotor(incremented_rotors[1])
        if(notch(incremented_rotors[1],incremented_rotors[2])):
            incremented_rotors[2]=shift_rotor(incremented_rotors[2])
    return incremented_rotors

def shift_ring(ring):
    return ring[-1]+ring[1:-1]

def shift_ring_n(ring,n):
    x=ring
    for i in range(n):
        x=shift_ring(x)
    return x


#Cipher or plain text
text='QBLTWLDAHHYEOEFPTWYBLENDPMKOXLDFAMUDWIJDXRJZDERFUEHRERISTTODXDERKAMPFGEHTWEITERXDOENITZXDERFUEHRERISTTODXDERKAMPFGEHTWEITERXDOENITZXDERFUEHRERISTTODXDERKAMPFGEHTWEITERXDOENITZXDERFUEHRERISTTODXDERKAMPFGEHTWEITERXDOENITZX'

#Rotors and keys settings
rotor1=rotor_number_v #Right most
rotor2=rotor_number_ii #Mid
rotor3=rotor_number_i #Left most
reflector=reflector_b
roter_key='BWX'
ringsetting_key='NVF'
plugboard=['PO', 'ML', 'IU', 'KJ', 'NH', 'YT','GB', 'VF', 'RE', 'DC']

rotors= [rotor1,rotor2,rotor3]
rotors= [shift_rotor_n(rotors[i],abc.find(roter_key[i])) for i in range(len(rotors))] 
rotors= [[rotors[i][0],rotors[i][1],rotors[i][2],abc.find(ringsetting_key[i])] for i in range(len(rotors))]

text=text.upper().replace(' ','')

for plug in plugboard:
    text=swap(text,plug)

result=''

for counter in range(len(text)):
    rotors=incr_rotors(rotors)
    t=text[counter]

    #print(t,end='')
    for rotor in rotors:
        t=rot(t,-rotor[3])
        t=rotor[0][abc.find(t)]
        t=rot(t,-rotor[2])
        t=rot(t,rotor[3])
        #print(t,end='')

    t=reflector[abc.find(t)]
    #print(t,end='')

    for rotor in rotors[::-1]:
        t=rot(t,-rotor[3])
        t=rot(t,rotor[2])
        t=abc[rotor[0].find(t)]
        t=rot(t,rotor[3])
        #print(t,end='')
    
    result+=t
    
    #print(t)
    
for plug in plugboard:
    result=swap(result,plug)
    
print(result)