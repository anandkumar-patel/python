# Example file for working with conditional statement
#


def main():
    x, y = 8, 8

    if x < y:
        st = "1 if : x is less than y"

    elif x == y:
        st = "1 elif : x is same as y"

    else:
        st = "1 else : x is greater than y"
    print(st)


if __name__ == "__main__":
    main()


# How to execute conditional statement with minimal code
def main():
    x, y = 10, 8
    st = "2 if : x is less than y" if (x < y) else "2 else : x is greater than or equal to y"
    print(st)


if __name__ == "__main__":
    main()

# Nested IF Statement
total = 10
# country = "US"
country = "US"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")

if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")


# Switch Statement
def switch_example(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 2
    print(switch_example(argument))
