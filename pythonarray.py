# Array in python 
import array as arr
marks=arr.array('i',[45,68,76,56,89,88,92,98])
print(marks)
marks.append(20)
print(marks)
marks.remove(68)
print("highest marks:",max(marks))
print("lowest marks:",min(marks))
print("total marks:",sum(marks))

