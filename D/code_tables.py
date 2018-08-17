def code_table_e(text, table_dict, bin_swap_dict, bin_code=False, delimiter = " "):
    from common import replace_all
    converted=""

    for s in text[:]:
        if s in table_dict:
            converted+=table_dict[s] + delimiter
        else:
            converted+=s + delimiter
    
    if bin_code:
        converted=replace_all(converted,bin_swap_dict)
    
    return converted

def code_table_d(text, table_dict, bin_swap_dict, bin_code=False, delimiter=" "):
    from common import replace_all
    if bin_code:
        table_dict_inv = dict((replace_all(j,bin_swap_dict),i) for (i,j) in table_dict.items())
    else:
        table_dict_inv = dict((j,i) for (i,j) in table_dict.items())
    
    code_string = text.split(delimiter)
    converted=""
    for s in code_string:
        if s in table_dict_inv:
            converted+=table_dict_inv[s]
        elif len(s)>0:
            converted+="[" + s + "]"
    
    return converted        




list_A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_a=list_A.lower()
list_0="0123456789"
list_0_for_atbash="123456789"

morse_code_table = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
     	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',  '4': '....-',  
        '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', '9': '----.', 
        '.' : '.-.-.-', ',' : '--..--', ':' : '---...', '?' : '..--..',
        "'" : '.----.', '-' : '-....-', '/' : '-..-.', '@' : '.--.-.', '=' : '-...-',
        ' ' : '/'
        }
        
bacon1_table = {
        'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaaa', 
        'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab', 
        'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba', 
        'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab', 'Y':'babba', 'Z':'babbb',
        ' ' : '/'
        }

bacon2_table = {
        'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab',
        ' ' : '/'
        }


