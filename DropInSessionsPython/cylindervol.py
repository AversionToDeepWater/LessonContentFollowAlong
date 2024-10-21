"""
Water Tank Filling Challenge

You have a cylindrical water tank that is partially filled with water.
Given the radius and height of the tank, and the current height of the water inside,
write a function that calculates the volume of water in the tank.

Problem:
Given the radius "r" of the cylinder and the height "h" of the water (both in meters),
write a Python function to calculate the volume of water in cubic meters.

CONSTRAINT:
    If the value of either radius or water_height is negative or invalid a CUSTOM Exception
    should be raised!!


Examples Input:
radius = 3
water_height = 4

Expected Output:
113.09733552923255

"""
from math import pi
radius = 0.03
water_height = 0.04


def cylinder_volume (radius:float, water_height:float) -> float:
    if type(radius) is str or type(water_height) is str:
        print("Invalid input")
        return None

    if radius < 0 or water_height < 0:
        print("Please enter a positive value")
        return None
    try:
        radius_squared = radius ** 2
        volume = radius_squared * pi * water_height
        return volume
    except TypeError:
        print("Please input a number")
        return None




print(cylinder_volume(radius, water_height))

if __name__ == "__main__":
    pass


