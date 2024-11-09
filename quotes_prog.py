with open("quotes.txt", "r", encoding="utf-8") as sigma:
    data = sigma.read()

print(data)

ansver input("ваше призвище?")

with open("quotes.txt", "r", encoding="utf-8") as sigma:
    sigma.write("\n" + answer)

    with open("quotes.txt", "r", encoding="utf-8") as sigma:
    data = sigma.read()

    print()
