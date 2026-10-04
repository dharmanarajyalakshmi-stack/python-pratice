# python collection
# python list
l=["apple","banana","mango","orange"]
print(l)
l.append("cherry")
l.insert(3,"grapes")
l.extend(["kiwi","melon"])
l[2]="pineapple"
l.remove("banana")
l.pop(2)
print(l.index("apple"))  
l.sort()
l.reverse()
len(l)
num=[10,20,30,40,50,60]
print(num.count(40))
l.clear()


# python tuple 
t=("place","things","animals","fruits","vegtables","groceries")
print(t)
print(t[3])
print(t[-4])
print(t.count("animals"))
print(t.index("vegtables"))
print("groceries" in t)
a=(2,4,5,3,6,7,)
b=(1,6,8,9,0,11)
c=a+b
print(t)
num=(1,2)
print(num*3)

# set in python collection
s={"python","c","c++","data science"}
s.add("Machine Learning")
s.update({"SQL","data science"})
s.remove("c++")
s.discard("c")
new_copy=s.copy()
new_s=s.copy()
new_s.clear()
#set operations 
A={1,3,45,6,7,43,7,2,67,7}
B={3,3,1,5,7,3,8,9,3,9,4,}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

# dictionary in python collection 
ST={"name":"Raji","age":21,"city":"hyderabad","college":"VIT"}
print(ST["name"])
print(ST.get("age"))

ST["city"]="vizag"
print(ST)
ST.update({"age":22})
del ST["city"]
print(ST)
print("name" in ST)
ST.keys()
ST.values()
ST.items()
ST.pop("college")
