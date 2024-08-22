from dataclasses import asdict, dataclass

@dataclass
class UserPayload:
    name:str
    last_name:str
    email:str

    def to_dict(self):
        return asdict(self)
