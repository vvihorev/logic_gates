class LogicGate:
    def __init__(self) -> None:
        self.output = None

    def get_output(self):
        self.perform_logic()
        return self.output


class NotGate(LogicGate):
    def __init__(self) -> None:
        super().__init__()
        self.pin = None
    
    def set_input(self, value):
        self.pin = value

    def perform_logic(self):
        self.validate_input()
        if self.pin == 1:
            self.output = 0
        else:
            self.output = 1

    def validate_input(self):
        if self.pin is None:
            raise ValueError('Input is None')


class AndGate(LogicGate):
    def __init__(self) -> None:
        super().__init__()
        self.pin_a = None
        self.pin_b = None
    
    def set_input(self, value):
        if self.pin_a is None:
            self.pin_a = value
        elif self.pin_b is None:
            self.pin_b = value

    def perform_logic(self):
        self.validate_input()
        self.output = self.pin_a & self.pin_b

    def validate_input(self):
        if self.pin_a is None or self.pin_b is None:
            raise ValueError('Input is None')
