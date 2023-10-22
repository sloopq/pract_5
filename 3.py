n = int(input("Введите количество названных городов: "))
my_set = set()


for i in range(n):
    city = input()
    my_set.add(city)

while True:
    city = input("Введите город (или 'stop' для завершения): ")

    if city == "stop":
        break

    if city not in my_set:
        my_set.add(city)
        print("OK")
    else:
        print("REPEAT")
