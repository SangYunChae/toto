from fastapi import APIRouter, Path, HTTPException
from model import GuestbookEntry
from typing import List
from datetime import datetime

guestbook_router = APIRouter()

guestbook_entries: List[GuestbookEntry] = []

@guestbook_router.post("/guestbook")
async def add_entry(entry: GuestbookEntry) -> dict:
    entry.id = len(guestbook_entries) + 1
    entry.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guestbook_entries.append(entry)
    return {"msg": "Entry added successfully"}

@guestbook_router.get("/guestbook")
async def retrieve_entries() -> dict:
    return {"entries": guestbook_entries}

@guestbook_router.delete("/guestbook/{entry_id}")
async def delete_entry(entry_id: int = Path(..., title="The ID of the entry to delete")) -> dict:
    for index, entry in enumerate(guestbook_entries):
        if entry.id == entry_id:
            del guestbook_entries[index]
            return {"msg": f"Entry with ID {entry_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Entry not found")
