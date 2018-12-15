

def part1(freq_changes):
    cur_freq = 0

    for freq_change in freq_changes:
        cur_freq += int(freq_change)

    print("End freq : {}".format(cur_freq))

def part2(freq_changes):
    freqs_already_reached = [0]
    cur_freq = 0

    while True:
        for freq_change in freq_changes:
            cur_freq += int(freq_change)
            if cur_freq in freqs_already_reached:
                print("{} reached twice".format(cur_freq))
                return
            else:
                freqs_already_reached.append(cur_freq)


def main():
    with open("input", "r") as f:
        freq_changes = f.read().split("\n")
    part1(freq_changes)
    part2(freq_changes)
    
if __name__ == "__main__":
    main()