from basic_gates import BinaryGate, AndGate, NotGate, OrGate, Connector


class NandGate(BinaryGate):
    def __init__(self) -> None:
        super().__init__()
        self.ag = AndGate()
        self.ng = NotGate()
        self.c = Connector(self.ag, self.ng)

    def perform_logic(self):
        self.ag.set_input(self.pin_a)
        self.ag.set_input(self.pin_b)
        self.output = self.ng.get_output()


class XorGate(BinaryGate):
    def __init__(self) -> None:
        super().__init__()
        self.nag = NandGate()
        self.og = OrGate()
        self.ag = AndGate()
        self.c1 = Connector(self.nag, self.ag)
        self.c1 = Connector(self.og, self.ag)
    
    def perform_logic(self):
        self.og.set_input(self.pin_a)
        self.og.set_input(self.pin_b)
        self.nag.set_input(self.pin_a)
        self.nag.set_input(self.pin_b)
        self.output = self.ag.get_output()