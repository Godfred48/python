"""Here is another solution. This solution organizes the data about
the cans in a compound list. A compound list is a list that contains
lists. CSE 111 students study lists and compound lists in lesson 7.

def main():
    # A compound list (a list that contains lists).
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the can_sizes list, unpack the values
    # into the variables name, radius, height, and cost.
    for name, radius, height, cost in can_sizes:
        .
        .
        .
"""
import math 

#function for calculating volumes for can
def can_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

#function for calculating surface area for can
def can_surface_area(radius, height):
    surface_area = (2* math.pi * radius) * (radius + height)
    return surface_area

def storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency


def main():
    can_names = [
            "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
            "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
        ]
    can_radiuses = [
            6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
            5.4, 6.83, 15.72, 6.83, 7.62, 8.1
        ]
    can_heights = [
            10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
            8.89, 7.62, 17.78, 12.38, 11.27, 11.11
        ]
    can_costs = [
            0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
            0.22, 0.26, 1.53, 0.34, 0.38, 0.42
        ]

    max_efficiency = -1

    print("=" *50)
    print("Can Storage Efficiency Report")
    print("=" *50)

    for i in range(len(can_names)):
        volume = can_volume(can_radiuses[i], can_heights[i])
        surface_area = can_surface_area(can_radiuses[i], can_heights[i])
        efficiency = storage_efficiency(volume, surface_area)

        print(f"Can Name: {can_names[i]}")
        print(f"Volume: {volume:.2f} cubic units")
        print(f"Surface Area: {surface_area:.2f} square units")
        print(f"Storage Efficiency: {efficiency:.2f}")
        print(f"Cost: ${can_costs[i]:.2f}")
        print("-" *50)

        if efficiency > max_efficiency:
            max_efficiency = efficiency
            canName = can_names[i]
    print(f"Maximum Storage Efficiency: {max_efficiency:.2f}")
    print(f"Name of Can: {canName}")
    print("=" * 50)

main()