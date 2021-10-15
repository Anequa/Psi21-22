# zad5
# dwróconą kolejnością znaków z
# kapitalikami. Np. Fotzsyzrk Kaipor
name = ["Weronika", "Krejner"]
print(name[0][::-1].lower().capitalize(), name[1][::-1].lower().capitalize())

print("zad6")
numbers_to_10 = [i + 1 for i in range(10)]
second_half = numbers_to_10[5:]
numbers_to_10 = numbers_to_10[:5]

print(numbers_to_10)
print(second_half)

print("zad7")
numbers_to_10 += second_half
numbers_to_10.insert(0, 0)
print(numbers_to_10)

copy_of_numbers = sorted(numbers_to_10.copy(), reverse=True)
print(numbers_to_10)
print(copy_of_numbers)
