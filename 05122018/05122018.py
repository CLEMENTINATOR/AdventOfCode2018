def reacts(c1, c2):
    return (c1.lower() == c2 and c2.upper() == c1) or (c2.lower() == c1 and c1.upper() == c2)

def part1(polymer):
    while(True):
        match_found = False
        for i in range(0, len(polymer) - 1):
            if reacts(polymer[i], polymer[i + 1]):
                polymer = polymer[:i] + polymer[i+2:]
                match_found = True
                break

        if not match_found or not len(polymer):
            break

    print("Resulting polymer len: {}".format(len(polymer)))

def main():
    with open("input", "r") as f:
        polymer = f.read()

    part1(polymer)


if __name__ == "__main__":
    main()