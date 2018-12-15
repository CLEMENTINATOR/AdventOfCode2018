

def part1(freq_changes):
    cur_freq = 0

    for freq_change in freq_changes:
        cur_freq += int(freq_change)

    print("End freq : {}".format(cur_freq))


def main():
    with open("input", "r") as f:
        freq_changes = f.read().split("\n")
    part1(freq_changes)
    
if __name__ == "__main__":
    main()