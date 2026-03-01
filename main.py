from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "签证查询API"}
@app.get("/requirements")
def requirements(country: str = ""):
    return {"success": True, "documents": ["护照", "照片"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
