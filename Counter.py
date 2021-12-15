class CounterConfig:
    def __init__(self):
        self.pc = 0

    def hash(self):
        return hash(self.pc)

    