from i_sink import ISink
import json

class ConsoleSink(ISink):

    def __init__(self):
        pass

    def sink_data(self, data: dict) -> None:
        data_json = json.dumps(data)
        print(data_json)