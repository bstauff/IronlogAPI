import uuid


class Lift:
    def __init__(self, id: uuid.UUID, name: str, training_max: int):
        self.__id = id
        self.__name = name
        self.__trainingmax = training_max
