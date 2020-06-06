from functools import reduce

capacities = [
    320,
    160,
    80,
    40,
    20,
    10,
]

machine_types = [
    "10XLarge",
    "8XLarge",
    "4XLarge",
    "2XLarge",
    "XLarge",
    "Large",
]

costs ={
    'New York': [2820, 1400, 774, 450, 230, 120],
    'India': [2970, 1300, 890, 413, None, 140],
    'China': [None, 1180, 670, None, 200, 110]
}

def get_input(input_val=None):
    x = input_val or input('Enter Input:\n')
    numbers = []
    for word in x.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers

def calculate_all_possible(zipped_list, capacity, values_list=[]):
    if len(zipped_list):
        if zipped_list[0][3]:
            for value in range(zipped_list[0][2]+1):
                calculate_all_possible(zipped_list[1:], capacity, [*values_list, value])
        else:
            calculate_all_possible(zipped_list[1:], capacity, [*values_list, 0])
    else:
        if reduce(lambda y,z: y+z, map(lambda x:x[0]*x[1], zip(capacities, values_list))) == capacity:
            # print Each possible list to console
            # print(values_list)
            empty_list.append(values_list)

def calculate_minimum(location):
    global empty_list
    empty_list = []
    calculate_all_possible(machine_zip[location], capacity)
    print(len(empty_list))
    mapped = map(lambda x: reduce(lambda p,q: p+q, map(lambda y: y[0]*y[1], filter(lambda x: x[1], zip(x, costs[location])))), empty_list)
    list_map = list(mapped)
    list_min = min(list_map)
    return empty_list[list_map.index(list_min)], list_min

def get_out():
    out_dict = {
        "Output": []
    }
    for loc in ['New York', 'India', 'China']:
        min_list, minimum = calculate_minimum(loc)
        out_dict["Output"].append({
          "region": loc,
          "total_cost": minimum * hour,
          "machines": list(filter(lambda x: x[1], zip(machine_types, min_list)))
        })
    print(out_dict)
    return out_dict

def main(input_val=None):
    global capacity, hour, max_resources, machine_zip
    capacity, hour = get_input(input_val)
    max_resources = [capacity//cap for cap in capacities]

    machine_zip = {
        'New York': list(zip(capacities, machine_types, max_resources, costs['New York'])),
        'India': list(zip(capacities, machine_types, max_resources, costs['India'])),
        'China': list(zip(capacities, machine_types, max_resources, costs['China']))
    }
    return get_out()

if __name__ == '__main__':
    main()
