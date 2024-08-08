from dataclasses import dataclass

@dataclass
class UserModel:
    id:int
    name:str
    last_name:str
    email:str
