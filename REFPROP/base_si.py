from enum import Enum

class BASE_SI(Enum):
    MASS_SI = "MASS BASE SI"
    MOLAR_SI = "MOLAR BASE SI"

    def __str__(self) -> str:
        return self.value