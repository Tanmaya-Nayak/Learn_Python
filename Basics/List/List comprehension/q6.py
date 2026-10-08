# Nested if with List Comprehension
basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith("a")])
