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
async def choose_college(college_choice: CollegeChoice):
    chosen_college = college_choice.college_name
    # Assuming you have some database connection or ORM set up
    # You can save the chosen college to your database here
    # For demonstration purposes, let's just print it
    print(f"Chosen college: {chosen_college}")
    return {"message": f"You chose {chosen_college}!"}
