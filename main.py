from fastapi import FastAPI

app = FastAPI()


students = {
    1:{
        "name":"John",
        "age":16,
        "class":9
    }
}


@app.get('/')
    
def index():
    return {'name':"Arnab"}

@app.get("/get-student/{student_id}")
# def get_student(student_id: int = Path(None, description = 'the id of the student you want to view',gt=0)):
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}