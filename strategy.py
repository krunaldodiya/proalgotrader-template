from pyalgotrader_protocols import Algorithm_Protocol


class Strategy(Algorithm_Protocol):
    async def initialize(self):
        print("init")

    async def next(self):
        print("next")
