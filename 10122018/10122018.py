import parse

class Stars(object):
    _format = parse.compile("position=<{},{}> velocity=<{},{}>")

    def __init__(self, star_data_str):
        r = Stars._format.parse(star_data_str)
        self._x = int(r[0])
        self._y = int(r[1])
        self._spe_x = int(r[2])
        self._spe_y= int(r[3])

    def move(self):
        self._x += self._spe_x
        self._y += self._spe_y

    def has_position(self, x, y):
        return self._x == x and self._y == y

    def __str__(self):
        return "({},{})".format(self._x, self._y)

    def distance(self, star2):
        return abs(star2._x - self._x) + abs(star2._y - self._y)

    def __eq__(self, star2):
        return star2._x == self._x and star2._y == self._y

def part1(stars):
    time_elapsed = 0
    while time_elapsed != 10880:
        time_elapsed += 1
        for star in stars:
            star.move()

    min_star_x = min(stars, key=lambda s: s._x)._x
    min_star_y = min(stars, key=lambda s: s._y)._y
    max_star_x = max(stars, key=lambda s: s._x)._x
    max_star_y = max(stars, key=lambda s: s._y)._y
    for j in range(min_star_y, max_star_y + 1):
        for i in range(min_star_x, max_star_x + 1):
            found = False
            for star in stars:
                if star.has_position(i,j):
                    print("#", end="")
                    found = True
                    break
            if not found:
                print(".", end="")
        print("")

def main():
    stars = []
    with open("input", "r") as f:
        stars_data_str = f.read().split("\n")
    for star_data_str in stars_data_str:
        stars.append(Stars(star_data_str))

    part1(stars)

if __name__ == "__main__":
    main()