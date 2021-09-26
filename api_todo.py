from flask import Flask
from flask_restful import reqparse, abort, fields, marshal_with, marshal, Api, Resource, request

app = Flask(__name__)
api = Api(app)

TODOS = [
    {'task': 'prepare for exam'},
    {'task': 'apply for bank loan', 'otherField': 'secret data!', },
    {'task': 'time for bed'},
]

# only output the ‘task’ field
fields = {
    'task': fields.String
}


# show a single item and lets you delete it
class Todo(Resource):
    @marshal_with(fields)
    def get(self, todo_id):
        if len(TODOS) == 0 or todo_id >= len(TODOS):
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        return TODOS[todo_id]

    def delete(self, todo_id):
        if len(TODOS) == 0 or todo_id >= len(TODOS):
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        TODOS.pop(todo_id)
        return "", 204


# shows a list of all todos, POST to add new tasks, and PUT to edit a task
class TodoList(Resource):
    @marshal_with(fields)
    def get(self):
        return TODOS

    def put(self):
        args_id = request.args.get('id', type=int)
        args_task = request.args.get('task')
        TODOS[args_id] = {'task': args_task}
        return marshal(TODOS[args_id], fields), 201

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task', type=str)
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS.append(task)
        return marshal(task, fields), 201


# Setup the Api resource routing here
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
