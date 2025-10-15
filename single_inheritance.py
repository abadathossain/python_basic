class GrandPa:
    def __init__(self,color,name):
        self.color=color
        self.name=name

class Father(GrandPa):
    def __init__(self,hobby,color,name):
        self.hobby=hobby
        super().__init__(color,name)

gf1=GrandPa("Red","khan")
f1=Father("Ball","Green","Khan")
print(f"Name: {gf1.name}, Liked: {gf1.color}")
print(f"F Name: {f1.name}, F Liked: {f1.color}")