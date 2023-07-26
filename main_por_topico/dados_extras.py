from datetime import datetime, timedelta, time
from typing import Union
from uuid import UUID
from fastapi import FastAPI, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def read_item(
        item_id: int,
        start_datetime: Union[datetime, None] = Body(default=None),
        end_datetime: Union[datetime, None] = Body(default=None),
        repeat_at: Union[time, None] = Body(default=None),
        process_after: Union[timedelta, None] = Body(default=None)
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }
