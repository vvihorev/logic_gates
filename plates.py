from basic_gates import AndGate, BinaryGate
from complex_gates import XorGate


class HalfAdder(BinaryGate):
    def __init__(self) -> None:
        super().__init__()
        self.xg = XorGate()
        self.ag = AndGate()
        self.value = None
        self.carry = None
    
    def perform_logic(self):
        self.xg.set_input(self.pin_a)
        self.xg.set_input(self.pin_b)
        self.ag.set_input(self.pin_a)
        self.ag.set_input(self.pin_b)
        self.value = self.xg.get_output()
        self.carry = self.ag.get_output()
    
    def get_value(self):
        self.perform_logic()
        return self.value

    def get_carry(self):
        self.perform_logic()
        return self.carry