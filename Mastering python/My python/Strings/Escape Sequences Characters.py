# ---------------------------------
# Escape Sequences Characters
# \b => Back Space 
# \newline => Escape New Line + \ 
# \\ => Escape Back Slash 
# \' => Escape single Quotes 
# \" => Escape Double Quotes 
# \n => Line Feed 
# \r => Carriage Return 
# \t => Horizontal Tab 
# \xhh => charcter Hex Value 
# ----------------------------------

# Back Space  
print("Hello\bWorld") # Will Remove o 

# Escape New Line + Back Slash 
print("Hello \
I Love \
python ") # Hello I Love python                        

# Escape Back Slash 
print("I Love Back Slash\\") # I Love Back Slash\

# Escape single Quotes  
print('I Love single Quotes \'test\'') #I Love Double Quotes \'test\'

# Escape Double Quotes  
print("I Love Double Quotes \"test\" ") #I Love Double Quotes \"test\"

# Line Feed              
print("Hello\nWorld")   #Hello  
                        #World                          
# Carriage Return 
print("123456\rbcde") #bsde56

# Horizontal Ta
print("Hello\tWorld") #Hello  World b

# charcter Hex Value 
print("\x57\x41\x4C\x49\x44") #walid