def my_func(**kwargs):
    print(kwargs)
    print(f"My name:{kwargs['name']}. Age:{kwargs['age']} and address={kwargs["address"]}")

my_func(name="Abadat",age=37, address="CTG")