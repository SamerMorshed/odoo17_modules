import { Component, useState } from '@odoo/owl';
import { useService } from '@odoo/owl/dist/hooks/useService';

class TodoApp extends Component {
    todoService = useService('todo');
    setup() {
        this.state = useState({
            todos: [],
            inputVal: '',
            selectedDate: new Date().toISOString().slice(0, 10),
        });
        this.loadTodos();
    }

    async loadTodos() {
        this.state.todos = await this.todoService.getTodos(this.state.selectedDate);
    }

    async addTodo() {
        await this.todoService.createTodo(this.state.inputVal, this.state.selectedDate);
        this.state.inputVal = '';
        await this.loadTodos();
    }

    async toggleDone(todo) {
        await this.todoService.toggleDone(todo);
        await this.loadTodos();
    }

    onDateChange(e) {
        this.state.selectedDate = e.target.value;
        this.loadTodos();
    }
}

TodoApp.template = 'todo_app.template';
TodoApp.components = {};

export default TodoApp;