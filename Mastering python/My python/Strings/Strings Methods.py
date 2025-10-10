# -----------------------------------------
# --- String  Methods ---------------------
# -----------------------------------------

# Strings() rstrip() lstrip() 

a = "    I love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

b = "####I love Python####"
print(b.strip("#"))
print(b.strip("#"))
print(b.strip("#")) 

c = "#@#@I love Python@#@#"
print(c.strip("#@"))
print(c.strip("#@"))
print(c.strip("#@"))

# title() 
d = "i love python and php and 4k"
print(d.title())

# capitalize()
e = "i love python and php and 4k"
print(e.capitalize())
