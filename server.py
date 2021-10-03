from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    employee = {"name": "carmel", "age": 25, "salary": 100}
    return employee


@app.route("/user/<name>", methods=['GET', 'POST', 'DELETE'])
def hello_user(name):
    employee = {"name": name, "age": 25, "salary": 100}
    if request.method == 'GET':
        return employee
    if request.method == 'POST':
        employee['age'] = 12
        return employee
    if request.method == 'DELETE':
        return {"message": "Successfully! Record has been deleted"}
    else:
        return "Record not found", 400


if __name__ == '__main__':
    app.run()
