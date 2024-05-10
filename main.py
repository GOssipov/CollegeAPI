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

@app.get("/chosen_college/{college_name}")
async def chosen_college(college_name: str):
    if college_name in college_names:
        return {"chosen_college": college_name}
    else:
        return {"error": "College not found"}
