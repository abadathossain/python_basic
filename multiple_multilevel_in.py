# multilevel example
# --------------------------

# class Grandpa:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

# class Father(Grandpa):
#     def __init__(self,hobby, name, color):
#         super().__init__(name, color)
#         self.hobby=hobby

# class Children(Father,Grandpa):
#     def __init__(self, hobby, name, color):
#         super().__init__(hobby, name, color)

# gf1=Grandpa("Khan","Red")
# c1=Children("Ball","Karim", "Green")
# print(gf1.name,gf1.color)
# print(c1.name,c1.hobby,c1.color)



# multiple example
# --------------------------
class Grandpa:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Father():
    def __init__(self,hobby):
        self.hobby=hobby

class Children(Father,Grandpa):
    def __init__(self,fashion, hobby, name, color):
        self.fashion=fashion
        Father.__init__(self,hobby)
        Grandpa.__init__(self, name,color)

# gf1=Grandpa("Khan","Red")
# c1=Children("Ball","Karim", "Green")
# print(gf1.name,gf1.color)
# print(c1.name,c1.hobby,c1.color)

c2=Children("Test","Ball","Karim", "Green")
print(c2.fashion,c2.hobby,c2.name,c2.color)