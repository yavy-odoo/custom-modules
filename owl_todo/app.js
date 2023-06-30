const { Component, mount, xml, useRef, onMounted, useState, reactive, useEnv } =
  owl;

// -------------------------------------------------------------------------
// Task Component
// -------------------------------------------------------------------------
class Task extends Component {
  deleteTask() {
    this.props.onDelete(this.props.task);
  }

  toggleTask() {
    this.props.task.isCompleted = !this.props.task.isCompleted;
  }

  static template = xml/* xml */ `
        <div class="task" t-att-class="props.task.isCompleted ? 'done' : ''">
            <input type="checkbox" t-att-checked="props.task.isCompleted" t-on-click="toggleTask"/>
            <span><t t-esc="props.task.text"/></span>
            <span class="delete" t-on-click="deleteTask">🗑</span>
        </div>`;
  static props = ["task", "onDelete"];
}

// -------------------------------------------------------------------------
// Root Component
// -------------------------------------------------------------------------
class Root extends Component {
  nextId = 0;
  tasks = useState([]);

  deleteTask(task) {
    const index = this.tasks.findIndex((t) => t.id === task.id);
    this.tasks.splice(index, 1);
  }

  addTask(ev) {
    // 13 is keycode for ENTER
    if (ev.keyCode === 13) {
      const text = ev.target.value.trim();
      ev.target.value = "";
      console.log("adding task", this.tasks);
      this.tasks.push({
        id: this.nextId++,
        text,
        isCompleted: false,
      });
    }
  }

  static template = xml/* xml */ `
    <div class="todo-app">
        <input placeholder="Enter a new task" t-on-keyup="addTask"/>
        <div class="task-list">
            <t t-foreach="tasks" t-as="task" t-key="task.id">
                <Task task="task" onDelete.bind="deleteTask"/>
            </t>
        </div>
    </div>`;
  static components = { Task };
}

// -------------------------------------------------------------------------
// Setup
// -------------------------------------------------------------------------
mount(Root, document.body, { dev: true });
