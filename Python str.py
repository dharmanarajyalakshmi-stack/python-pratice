# performing string slicing techniques 
Str= "Python Programming Language" 
print(type(Str))
  # indexing 
print(Str[8:23])
print(Str[7:15])
# reverse indexing
print(Str[-14:-7])
print(Str[ :-3])
  #  slicing (start:end:step)
print(Str[6:20:2])
print(Str[0:13:3])
# searching 
print(Str.find("Language"))
print(Str.find("Program"))
print(Str.index("Lang"))       
if "Python" in Str:
 print("yes present")
else:
 print("not found")
# Replacing 
Text=Str.replace("Python Programming", "Full stack python")
print(Text)
# Substrings 
text = "Hello World"
print("World" in text)  

