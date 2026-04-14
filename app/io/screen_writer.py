from app.interfaces.i_output_writer import IOutputWriter


class ScreenWriter(IOutputWriter):

    def write(self, data: str) -> None:
        print(data)