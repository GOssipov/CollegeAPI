from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Landing Page"}

@app.get("/test")
async def root():
    return {"message":"Colleges Page"}
    
