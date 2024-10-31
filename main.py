import os
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from dotenv import load_dotenv

from urls import q_n_a_router

if os.environ.get("ENV", "local") == "local":
    load_dotenv()

app = FastAPI()
app.include_router(q_n_a_router, prefix="")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
