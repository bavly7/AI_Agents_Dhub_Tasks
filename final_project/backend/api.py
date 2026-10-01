from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from graph.workflow import build_graph
from database.db import create_table
import asyncio
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def startup():
    create_table()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html", encoding="utf-8") as f:
        return f.read()

@app.get("/run")
async def run_agents(query: str):
    async def event_stream():
        graph = build_graph()
        state = {
            "search_query": query,
            "leads": [],
            "qualified_leads": [],
            "emails_sent": 0
        }

        for step in graph.stream(state):
            yield f"data: {json.dumps(step)}\n\n"
            await asyncio.sleep(0.1)

        yield "data: {\"done\": true}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")