from dataclasses import dataclass


@dataclass
class Result:
    cpu: str
    monthly_cost: str
    memory: str
    storage: str
    bandwidth: str
