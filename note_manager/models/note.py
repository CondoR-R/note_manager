import dataclasses
import datetime as dt


@dataclasses.dataclass()
class Note:
    id: int
    title: str
    content: str
    tags: list[str] = dataclasses.field(default_factory=list)
    created_at: dt.datetime = dataclasses.field(default_factory=dt.datetime.now)
    updated_at: dt.datetime = dataclasses.field(default_factory=dt.datetime.now)
