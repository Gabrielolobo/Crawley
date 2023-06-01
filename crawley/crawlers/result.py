from dataclasses import dataclass


@dataclass
class Result:
    cpu: list
    monthly_cost: list
    memory: list
    storage: list
    bandwidth: list
