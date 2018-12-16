
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
    return polymer

def part2(polymer):
    poly_map = {}
    small_chars = [chr(item) for item in range(ord('a'), ord('z')+1)]

    for c in small_chars:
        if c not in polymer and c.upper() not in polymer:
            continue

        new_poly = polymer.replace(c, "").replace(c.upper(), "")
        new_poly_reacted = part1(new_poly)
        poly_map[c] = len(new_poly_reacted)

    smallest_poly_len = min(poly_map, key=lambda k: poly_map[k])
    print("Removing {} yeilds smallest length : {}".format(smallest_poly_len, poly_map[smallest_poly_len]))

def main():
    with open("input", "r") as f:
        polymer = f.read()

    part1(polymer)
    part2(polymer)

if __name__ == "__main__":
    main()