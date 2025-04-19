#!/bin/bash

# Start backend
uvicorn server.main:app --reload