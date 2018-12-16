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

def find_largest_total_power_region(fuel_cells, square_size_min=1, square_size_max=300):
    max_val = 0
    for s in range(square_size_min, square_size_max + 1):
        for x in range(0, 300 - s):
            for y in range(0, 300 - s):
                cur_val = 0
                for i in range(0,s):
                    for j in range(0,s):
                        cur_val += fuel_cells[x+i][y+j]
                if cur_val > max_val:
                    max_val = cur_val
                    max_x, max_y, max_s = x,y,s
    return (max_x, max_y, max_s, max_val)

def test():
    assert get_power_level(3, 5, 8) == 4
    assert get_power_level(122, 79, 57) == -5
    assert get_power_level(217, 196, 39) == 0
    assert get_power_level(101, 153, 71) == 4
    assert find_largest_total_power_region(generate_fuel_cells(18), 3, 3) == (33, 45, 3, 29)
    assert find_largest_total_power_region(generate_fuel_cells(42), 3, 3) == (21, 61, 3, 30)
    assert find_largest_total_power_region(generate_fuel_cells(18)) == (90, 269, 16, 113)
    assert find_largest_total_power_region(generate_fuel_cells(42)) == (232, 251, 12, 119)

def part1():
    part1_grid_id = 9445
    part1_fuel_cells = generate_fuel_cells(part1_grid_id)
    print(find_largest_total_power_region(part1_fuel_cells, 3, 3))

def part2():
    part1_grid_id = 9445
    part1_fuel_cells = generate_fuel_cells(part1_grid_id)
    print(find_largest_total_power_region(part1_fuel_cells))

def main():
    test()
    part1()
    part2()

if __name__ == "__main__":
    main()