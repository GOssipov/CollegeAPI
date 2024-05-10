from fastapi import FastAPI

app = FastAPI()

# Sample list of college names
college_names = ["College A", "College B", "College C"]

@app.get("/")
async def root():
    return {"message": "Landing Page Tester"}

@app.get("/current_college")
async def current_college():
    return college_names

@app.put("/choose_college")
async def choose_college(college_name: str):
    return {"message": f"You've chosen {college_name}"}
