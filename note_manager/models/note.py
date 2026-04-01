import dataclasses
import datetime


@dataclasses.dataclass()
class Note:
    id: int
    title: str
    content: str
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.now)
    updated_at: datetime.datetime = dataclasses.field(default_factory=datetime.now)
    tags: list[str] = dataclasses.field(default_factory=list)
