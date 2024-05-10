from fastapi import FastAPI

app = FastAPI()

# Sample list of college names
college_names = ["College A", "College B", "College C"]

@app.get("/")
async def root():
    return {"message": "Landing Page"}

@app.get("/current_college")
async def current_college():
    return college_names

@app.get("/chosen_college")
async def chosen_college():
    return college_names
