import pytest
from hypothesis import given
from hypothesis.strategies import integers

from airplane import services


class TestFuelConsumption:

    @given(integers(min_value=1), integers(min_value=1))
    def test_smoke(self, plane_id, passenger_capacity):
        """
        Different smoke test for calculate_fuel_consumption with different
        values generated from hypothesis
        """
        assert isinstance(
            services.calculate_fuel_consumption(plane_id, passenger_capacity),
            float)

    @pytest.mark.parametrize('plane_id,passenger_capacity', [(-1, 10), (10, -1), (0, -1)])
    def test_exception_cases(self, plane_id, passenger_capacity):
        with pytest.raises(ValueError):
            services.calculate_fuel_consumption(plane_id, passenger_capacity)


class TestCalculateFuelTank:

    @given(integers(min_value=1))
    def test_smoke(self, plane_id: int):
        """
        Different smoke test for calculate_fuel_tank with different
        values generated from hypothesis
        """
        assert isinstance(services.calculate_fuel_tank(plane_id), int)

    @pytest.mark.parametrize('plane_id', [-1, 0])
    def test_exception_cases(self, plane_id):
        with pytest.raises(ValueError):
            services.calculate_fuel_tank(plane_id)
