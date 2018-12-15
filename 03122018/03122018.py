import parse
from collections import defaultdict

SQUARE_SIZE = 1000

class Claim(object):
    _format = parse.compile("#{id} @ {x},{y}: {w}x{h}")
    def __init__(self, claim_str):
        r = Claim._format.parse(claim_str)
        self.id = int(r["id"])
        self.x = int(r["x"])
        self.y = int(r["y"])
        self.w = int(r["w"])
        self.h = int(r["h"])
        self.str = claim_str

    def to_1d_space(self):
        linear_space = defaultdict(int)
        for i in range(self.x, self.x + self.w):
            for j in range(self.y, self.y + self.h):
                linear_space[i + j * SQUARE_SIZE] = 1

        return linear_space

    def __str__(self):
        return self.str

def part1(claims):
    linear_space = defaultdict(int)
    for claim in claims:
        claim_space = claim.to_1d_space()
        for x in claim_space:
            linear_space[x] += 1

    overlaps = 0
    for elem in linear_space:
        if linear_space[elem] > 1:
            overlaps += 1

    print("overlaps: {}".format(overlaps))

def main():
    claims = []
    with open("input", "r") as f:
        claims_str = f.read().split("\n")
    for claim_str in claims_str:
        claims.append(Claim(claim_str))

    part1(claims)
    
    

if __name__ == "__main__":
    main()