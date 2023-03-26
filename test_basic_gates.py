import pytest

from basic_gates import NotGate, AndGate, OrGate, Connector, Source


S0 = Source(0)
S1 = Source(1)


@pytest.mark.parametrize(
    'pin,output',
    (
        (S0, 1),
        (S1, 0),
    )
)
def test_notgate(pin, output):
    ng = NotGate()
    ng.set_input(pin.get_output)
    assert ng.get_output() == output
    

@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (S0, S0, 0),
        (S0, S1, 0),
        (S1, S0, 0),
        (S1, S1, 1),
    )
)
def test_andgate(pin_a, pin_b, output):
    ag = AndGate()
    ag.set_input(pin_a.get_output)
    ag.set_input(pin_b.get_output)
    assert ag.get_output() == output


@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (S0, S0, 0),
        (S0, S1, 1),
        (S1, S0, 1),
        (S1, S1, 1),
    )
)
def test_orgate(pin_a, pin_b, output):
    og = OrGate()
    og.set_input(pin_a.get_output)
    og.set_input(pin_b.get_output)
    assert og.get_output() == output


@pytest.mark.parametrize(
    'pin_a,pin_b,output',
    (
        (S0, S0, 1),
        (S0, S1, 1),
        (S1, S0, 1),
        (S1, S1, 0),
    )
)
def test_connector(pin_a, pin_b, output):
    ag = AndGate()
    ag.set_input(pin_a.get_output)
    ag.set_input(pin_b.get_output)
    ng = NotGate()
    Connector(ag, ng)
    assert ng.get_output() == output