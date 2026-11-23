import { useRef } from "react";

function TaskManager({ tasks, saveTasks }) {
    const taskInput = useRef(null);
    const addTask = () => {
        const taskName = taskInput.current.value.trim();

        if (taskName === "") {
            alert("Please enter a task");
            return;
        }

        const newTask = {
            id: Date.now(),
            title: taskName,
            completed: false
        };
        const updatedTasks = [...tasks, newTask];
        saveTasks(updatedTasks);
        taskInput.current.value = "";
    };

    const toggleTask = (id) => {
        const updatedTasks = tasks.map(task =>
            task.id === id ? { ...task, completed: !task.completed }: task
        );
        saveTasks(updatedTasks);
    };

    const deleteTask = (id) => {

        const updatedTasks = tasks.filter(
            task => task.id !== id
        );

        saveTasks(updatedTasks);
    };

    
    const totalTasks = tasks.length;
    const completedTasks = tasks.filter(
        task => task.completed
    ).length;

    const pendingTasks = totalTasks - completedTasks;

    return (
        <div className="card">
            <h2>Task Manager</h2>
            <div className="task-input">
                <input
                    type="text"
                    placeholder="Enter your task"
                    ref={taskInput}
                    onKeyDown={(event) => {
                        if (event.key === "Enter") {
                            addTask();
                        }
                    }}
                />

                <button onClick={addTask}>
                    Add Task
                </button>

            </div>

            <div className="task-stats">

                <div>
                    <h3>{totalTasks}</h3>
                    <p>Total</p>
                </div>

                <div>
                    <h3>{completedTasks}</h3>
                    <p>Completed</p>
                </div>

                <div>
                    <h3>{pendingTasks}</h3>
                    <p>Pending</p>
                </div>

            </div>

            <div className="task-list">

                {tasks.length === 0 ? (

                    <p className="empty-message">
                        No tasks added yet.
                    </p>

                ) : (tasks.map(task => (
                        <div className="task-item" key={task.id}>
                            <span className={task.completed? "task-completed": ""}>{task.title}</span>
                            <div className="task-actions">
                                <button onClick={() => toggleTask(task.id)}>{task.completed? "Undo": "Complete"}</button>

                                <button className="delete-btn" onClick={() => deleteTask(task.id)}>Delete</button>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}

export default TaskManager;
