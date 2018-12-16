from collections import defaultdict

def get_new_point_id():
    chars = [chr(item) for item in range(ord('A'), ord('Z')+1)]
    for c in chars:
        yield c
    chars = [chr(item) for item in range(ord('a'), ord('z')+1)]
    for c in chars:
        yield c

class Point(object):
    generator = get_new_point_id()
    def __init__(self, coord_str, gen_id=True):
        coords = coord_str.split(",")
        self._x = int(coords[0])
        self._y = int(coords[1])
        if gen_id:
            self._id = next(Point.generator)

    @classmethod
    def __from_coordinates__(cls, x, y):
        return cls(Point.__to_str__(x, y), gen_id=False)

    def distance(self, point):
        return abs(self._x - point._x) + abs(self._y - point._y)

    @classmethod
    def __to_str__(cls, x, y):
        return "{}, {}".format(x, y)

    def __str__(self):
        return Point.__to_str__(self._x, self._y)

def part1(points):
    min_x = min(points, key=lambda k: k._x)._x
    max_x = max(points, key=lambda k: k._x)._x
    min_y = min(points, key=lambda k: k._y)._y
    max_y = max(points, key=lambda k: k._y)._y

    area_map = defaultdict(int)
    infinite_area = set()
    for y in range (min_y, max_y + 1):
        for x in range (min_x, max_x + 1):
            p = Point.__from_coordinates__(x, y)
            p_min_dist = None
            uniq = True

            for point in points:
                if not p_min_dist:
                    p_min_dist = point
                    uniq = True
                elif point.distance(p) < p_min_dist.distance(p):
                    p_min_dist = point
                    uniq = True
                elif point.distance(p) == p_min_dist.distance(p):
                    uniq = False

            if p._x == min_x or p._y == min_y or p._x == max_x or p._y == max_y:
                infinite_area.add(p_min_dist._id)

            if uniq:
                area_map[p_min_dist._id] += 1

    for infinite in infinite_area:
        del area_map[infinite]

    biggest_area = max(area_map, key=lambda k: area_map[k])
    print("biggest non infinite area size : {}".format(area_map[biggest_area]))

def main():
    points = []
    with open("input", "r") as f:
        coords_str = f.read().split("\n")
        for coord_str in coords_str:
            points.append(Point(coord_str))

    part1(points)





if __name__ == "__main__":
    main()