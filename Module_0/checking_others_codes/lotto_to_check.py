from random import randint

your_numbers = set()
draw = set()


def pass_numbers(your_numbers):
    while len(your_numbers) < 2:
        # tu jest mały błąd, bo jak bedziesz wpisywal non stop np.1 to masz nieskonczona petle, bo w set maja tylko unikalne elem.
        number = int(input(f'Wprowadź liczbę numer {(len(your_numbers)+1)} w zakresie od 1 do 49:')) # i tez powinienes ograniczyc to od 1 do 49
        your_numbers.add(number)
    return your_numbers

def draw_numbers(draw):
    draw.clear()
    while len(draw) < 2:
        draw.add(randint(1,50))
    return draw
#
def check():
    counter = 0
    while draw.issuperset(your_numbers) is False:
        draw_numbers(draw)
        print(draw)
        counter += 1
        print(counter)
    return counter

def message(counter):
    print(f'Wygrałeś za {counter} razem.')
    print(f'Jeśli puszczałbyś 7 kuponów tygodniowo, wygrałbyś za {int(counter/365)} lat. ')
    print(f'Koszt Twojej inwestycji wyniesie: {counter*3:,} PLN')

numbers = pass_numbers(your_numbers)
print(numbers)
draw = draw_numbers(draw)
print(draw)
counter = check()
print(counter)
message(counter)