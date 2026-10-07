import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "structured_logging" / "sinks"))

from file_sink import FileSink
from console_sink import ConsoleSink


def test_file_sink_writes_dict_as_json(tmp_path):
    target = tmp_path / "out.json"
    sink = FileSink(target)

    sink.sink_data({"id": 1, "city": "Reykjavík"})

    assert json.loads(target.read_text(encoding="utf-8")) == {"id": 1, "city": "Reykjavík"}


def test_console_sink_prints_dict_as_json(capsys):
    sink = ConsoleSink()

    sink.sink_data({"id": 1, "city": "Reykjavík"})

    printed = capsys.readouterr().out
    assert json.loads(printed) == {"id": 1, "city": "Reykjavík"}