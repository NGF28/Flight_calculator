import pytest

from flight_calculator import calculate_flight_time, flight_time_table


def test_calculate_flight_time_at_zero_weight():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_for_positive_weight():
    assert calculate_flight_time(100) == 170


def test_calculate_flight_time_for_fractional_weight():
    assert calculate_flight_time(12.5) == pytest.approx(178.75)


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        calculate_flight_time(-1)


def test_flight_time_table_returns_multiple_weight_entries():
    result = flight_time_table(20, 5)

    assert result == [
        (0.0, 180.0),
        (5.0, 179.5),
        (10.0, 179.0),
        (15.0, 178.5),
        (20.0, 178.0),
    ]


def test_flight_time_table_includes_maximum_weight():
    result = flight_time_table(10, 5)

    assert result[-1] == (10.0, 179.0)


def test_flight_time_table_returns_first_entry_when_step_exceeds_maximum():
    result = flight_time_table(3, 5)

    assert result == [(0.0, 180.0)]


def test_flight_time_table_returns_empty_list_for_negative_maximum_weight():
    result = flight_time_table(-1, 5)

    assert result == []


def test_flight_time_table_entries_are_in_ascending_weight_order():
    result = flight_time_table(15, 5)
    weights = [weight for weight, _ in result]

    assert weights == sorted(weights)
