def guess_number(number_range, tries, capital):

    from random import randint
    stop_toggle = 0
    new_capital = 0
    win_number = randint(number_range[0], number_range[1])
    print("Guess number.\n"
          f"Your capital: {capital}\n"
          f"Range: {number_range[0]} - {number_range[1]}\n"
          f"Make your choice.")

    for number in range(number_range[0], number_range[1] + 1):
        bid = input(f"Your bid for number {number}: ")
        if bid.lower() == "exit" or bid.lower() == "q" or bid.lower() == "quit" or bid.lower() == "e":
            stop_toggle = 1
            break
        else:
            bid = int(bid)
        if bid > capital:
            print("You don't have enough many for that bid.\n"
                  "We've taken the left money for that bid\n"
                  "Because you don't have money left, we stop taking your bid.")
            bid = capital
            capital = 0
            if number == win_number:
                new_capital += (bid * 2)
            break
        if number == win_number:
            new_capital += (bid * 2)
        capital -= bid
    new_capital += capital

    if stop_toggle == 1:
        print(f"Tries: {tries}\n"
              "Goodbye!")
    elif new_capital == 0:
        tries += 1
        print(f"You've lost."
              "Win-number: {win_number}\n"
              f"Tries: {tries}\n"
              "Goodbye!")
    else:
        tries += 1
        continue_or_not = input("Do you want to continue? Y/N\n").lower()
        if continue_or_not == "y" or continue_or_not == "yes":
            print(" ")
            guess_number(number_range, tries, new_capital)
        else:
            print(f"Tries: {tries}\n"
                  f"Capital: {new_capital}\n"
                  "Goodbye!")
