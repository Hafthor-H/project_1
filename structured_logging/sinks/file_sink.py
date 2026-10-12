from structured_logging.sinks.i_sink import ISink
import json
from pathlib import Path


class FileSink(ISink):

    def __init__(self, file_path: str | Path):
        self._filepath = Path(file_path)

    def sink_data(self, data: dict) -> None:

        with open(self._filepath, "a", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False,indent=2)
            file.write("\n")
    