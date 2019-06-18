list = ['a', 'b', 'c', 'd']
while True:
    try:
        letter = input("Enter: ").lower()
        print(list[list.index(letter) + 1])
    except IndexError:
        print(list[0])
