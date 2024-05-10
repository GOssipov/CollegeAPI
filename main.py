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

@app.route("/choose_college", methods=["GET", "PUT"])
async def choose_college(college_name: str = None):
    if college_name:
        return {"message": f"You've chosen {college_name}"}
    else:
        return {"message": "No college name provided"}
