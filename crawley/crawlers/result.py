from dataclasses import dataclass


@dataclass
class Result:
    process_unit: list
    memory: list
    storage: list
    transfer: list
    monthly_cost: list
