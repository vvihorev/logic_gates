import pytest

from basic_gates import Source
from complex_gates import NandGate, XorGate


S0 = Source(0)
S1 = Source(1)


@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (S0, S0, 1),
        (S0, S1, 1),
        (S1, S0, 1),
        (S1, S1, 0),
    )
)
def test_nandgate(pin_a, pin_b, output):
    nag = NandGate()
    nag.set_input(pin_a.get_output)
    nag.set_input(pin_b.get_output)
    assert nag.get_output() == output


@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (S0, S0, 0),
        (S0, S1, 1),
        (S1, S0, 1),
        (S1, S1, 0),
    )
)
def test_xorgate(pin_a, pin_b, output):
    xg = XorGate()
    xg.set_input(pin_a.get_output)
    xg.set_input(pin_b.get_output)
    assert xg.get_output() == output