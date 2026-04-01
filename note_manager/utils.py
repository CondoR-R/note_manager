import datetime as dt


def str_to_datetime(str_date: str) -> dt.datetime:
    return dt.datetime.fromisoformat(str_date)


def datetime_to_str(date: dt.datetime) -> str:
    return date.isoformat()
