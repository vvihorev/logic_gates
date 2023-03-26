import pytest

from main import NotGate, AndGate


@pytest.mark.parametrize(
    'pin,output',
    (
        (0, 1),
        (1, 0),
    )
)
def test_notgate(pin, output):
    ng = NotGate()
    ng.set_input(pin)
    assert ng.get_output() == output
    

@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
    )
)
def test_andgate(pin_a, pin_b, output):
    ag = AndGate()
    ag.set_input(pin_a)
    ag.set_input(pin_b)
    assert ag.get_output() == output