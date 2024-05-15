from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample list of college names
college_names = ["City College of San Francisco", "Canada College", "Skyline College", "San Mateo College", "Test College"]
major_names = ["Computer Science", "Data Science", "Computer Engineering", "Test Major"]

@app.get("/")
async def root():
    return {"message": "Landing Page Tester"}

@app.get("/current_college")
async def current_college():
    return college_names
    
@app.get("/current_major")
async def current_major():
    return major_names



class CollegeChoice(BaseModel):
    college_name: str

class MajorChoice(BaseModel):
    major_name: str

@app.post("/choose_college")
async def choose_college(college_choice: CollegeChoice):
    chosen_college = college_choice.college_name
    # Assuming you have some database connection or ORM set up
    # You can save the chosen college to your database here
    # For demonstration purposes, let's just print it
    print(f"Chosen college: {chosen_college}")
    return {"message": f"You chose {chosen_college}!"}

@app.post("/choose_major")
async def choose_major(major_choice: MajorChoice):
    chosen_major = major_choice.major_name
    # Assuming you have some database connection or ORM set up
    # You can save the chosen major to your database here
    # For demonstration purposes, let's just print it
    print(f"Chosen major: {chosen_major}")
    return {"message": f"You chose {chosen_major} as your major!"}
