import functools
import math

from airplane.const import FUEL_TANK_CONSTANT


@functools.lru_cache(maxsize=100)
def calculate_fuel_consumption(plane_id: int, passenger_capacity: int) -> float:
    if (plane_id <= 0) or (passenger_capacity <= 0):
        raise ValueError("Plane id or Passenger Capacity can not be less that 0."
                         " Plane id {}. Passenger capacity {}".format(plane_id, passenger_capacity))
    return (math.log(plane_id) * 0.8) + passenger_capacity * 0.002


@functools.lru_cache(maxsize=100)
def calculate_fuel_tank(plane_id: int) -> int:
    if plane_id <= 0:
        raise ValueError("Plane id can not be less that 0. Plane id {}".format(plane_id))
    return plane_id * FUEL_TANK_CONSTANT
