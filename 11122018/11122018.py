def get_power_level(x, y, grid_id):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_id
    power_level *= rack_id
    power_level = (power_level // 100)%10
    power_level -= 5
    return power_level

def generate_fuel_cells(grid_id):
    fuel_cells = [[get_power_level(x, y, grid_id) for y in range(300)] for x in range(300)]
    return fuel_cells

def find_largest_total_power_region(fuel_cells):
    max_val = 0

    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            cur_val = 0
            for i in range(0,3):
                for j in range(0,3):
                    cur_val += fuel_cells[x+i][y+j]
            if cur_val > max_val:
                max_val = cur_val
                max_x, max_y = x,y

    return max_x, max_y, max_val

def test():
    assert get_power_level(3, 5, 8) == 4
    assert get_power_level(122, 79, 57) == -5
    assert get_power_level(217, 196, 39) == 0
    assert get_power_level(101, 153, 71) == 4
    assert find_largest_total_power_region(generate_fuel_cells(18)) == (33, 45, 29)
    assert find_largest_total_power_region(generate_fuel_cells(42)) == (21, 61, 30)

def part1():
    part1_grid_id = 9445
    part1_fuel_cells = generate_fuel_cells(part1_grid_id)
    print(find_largest_total_power_region(part1_fuel_cells))

def main():
    test()
    part1()

if __name__ == "__main__":
    main()