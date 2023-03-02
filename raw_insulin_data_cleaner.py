import re

sequence = """ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

# Define the words and special characters to remove
words_to_remove = ['ORIGIN',"1","61"," "]
special_chars_to_remove = r'[//]'

# Use regex to remove the words and special characters from the sequence
clean_sentence = re.sub('|'.join(words_to_remove), '', sequence)
clean_sentence = re.sub(special_chars_to_remove, '', clean_sentence)

print(clean_sentence)

clean_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print("The length of the Clean sequence is "+ str(len(clean_sequence)))