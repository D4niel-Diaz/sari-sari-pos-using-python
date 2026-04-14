import json
from app.interfaces.i_input_reader import IInputReader


class FileReader(IInputReader):

    def __init__(self, filepath: str):
        self._filepath = filepath

    def read(self) -> dict:
        with open(self._filepath, "r") as f:
            data = json.load(f)
        return data