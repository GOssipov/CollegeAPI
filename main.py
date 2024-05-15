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

class CollegeChoice(BaseModel):
    college_name: str

@app.post("/choose_college")
def choose_college(college_choice: CollegeChoice):
    chosen_college = college_choice.college_name
    # Do something with the chosen college, like save it to a database
    return {"message": f"You chose {chosen_college}!"}
