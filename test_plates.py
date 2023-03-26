import pytest

from basic_gates import Source
from plates import HalfAdder


S0 = Source(0)
S1 = Source(1)


@pytest.mark.parametrize(
    'pin_a,pin_b,value,carry',
    (
        (S0, S0, 0, 0),
        (S0, S1, 1, 0),
        (S1, S0, 1, 0),
        (S1, S1, 0, 1),
    )
)
def test_halfadder(pin_a, pin_b, value, carry):
    ha = HalfAdder()
    ha.set_input(pin_a.get_output)
    ha.set_input(pin_b.get_output)
    assert ha.get_value() == value
    assert ha.get_carry() == carry