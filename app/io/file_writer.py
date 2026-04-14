from app.interfaces.i_output_writer import IOutputWriter


class FileWriter(IOutputWriter):

    def __init__(self, filepath: str):
        self._filepath = filepath

    def write(self, data: str) -> None:
        with open(self._filepath, "a") as f:
            f.write(data + "\n")