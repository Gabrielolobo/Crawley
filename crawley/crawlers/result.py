from dataclasses import dataclass


@dataclass
class Result:
    process_unit: str
    memory: str
    storage: str
    transfer: str
    monthly_cost: str
