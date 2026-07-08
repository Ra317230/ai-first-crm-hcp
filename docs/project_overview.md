# Project Overview

## Objective
Build an AI-first CRM HCP module that allows healthcare sales representatives to log interactions using either a structured form or an AI chat interface.

## Technologies
- React + Redux
- FastAPI
- LangGraph
- Groq (gemma2-9b-it)
- PostgreSQL/MySQL

## LangGraph Tools
1. Log Interaction
2. Edit Interaction
3. Search HCP
4. View Interaction History
5. Schedule Follow-up

## Workflow
User → React → FastAPI → LangGraph → Groq → Database → Response