def part1(box_ids):
    double_count = 0
    triple_count = 0

    for box_id in box_ids:
        chars_count = {}
        uniq_chars = set(box_id)
        for uniq_char in uniq_chars:
            chars_count[box_id.count(uniq_char)] = chars_count.get(box_id.count(uniq_char), 0) + 1
        if chars_count.get(2, 0):
            double_count += 1
        if chars_count.get(3, 0):
            triple_count += 1


    print("Checksum : {}".format(double_count * triple_count))

def main():
    with open("input", "r") as f:
        box_ids = f.read().split()
    part1(box_ids)
    
if __name__ == "__main__":
    main()