def k_func(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['name']}. I am {kwargs['age']} years old")

k_func(name="Khan", age=25)