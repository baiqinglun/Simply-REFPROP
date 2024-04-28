from enum import Enum

class Property(Enum):
    H="H"
    S="S"
    D="D"
    P="P"
    T="T"
    CV="CV"
    CP="CP"

    def __str__(self) -> str:
        return self.value