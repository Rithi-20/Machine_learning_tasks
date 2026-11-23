import { useState, useRef , useEffect} from "react";
import Navbar from "./components/Navbar";
import Calculator from "./components/calculator";
import TaskManager from "./components/TaskManager";
import "./App.css";
console.log(5);


function App() {
    console.log(6);
    const [, setRefresh]=useState(0);
    useEffect(()=> console.log(7),[]);

    const updateUI =() => {
        setRefresh(previous => previous + 1);
    };

    const appData = useRef({
    activeTab: "calculator",
    result: null,
    tasks: null
});

    if (appData.current.tasks === null) {
        const savedTasks =localStorage.getItem("reactlab_tasks");
        appData.current.tasks= savedTasks ? JSON.parse(savedTasks) : [];
    }

    const changeTab = (tab) => {
        appData.current.activeTab= tab;
        updateUI();
    };

    const calculate = (num1,num2,operator) => {
        let answer;

        switch (operator) {
            case "add":
                answer=num1+num2;
                break;

            case "subtract":
                answer=num1-num2;
                break;

            case "multiply":
                answer=num1*num2;
                break;

            case "divide":
                answer = num2 === 0 ? "Cannot divide by zero" : num1/num2;    
                break;

            default:
                answer = "Invalid operation";
        }

        appData.current.result=answer;
        updateUI();
    };

    const saveTasks = (updatedTasks) => {
        appData.current.tasks =updatedTasks;
 
        // localStorage can store only strings, not JavaScript arrays or objects , So convert the array into a string(Key,Value)
        localStorage.setItem("reactlab_tasks",JSON.stringify(updatedTasks));
        updateUI();
    };

    return (
        <div className="app">
            {console.log(8)}

            <h1 className="app-title">Calculator</h1>

            <Navbar
                activeTab={appData.current.activeTab}
                changeTab={changeTab}
            />

            {appData.current.activeTab === "calculator" && (
                <Calculator
                    calculate={calculate}
                    result={appData.current.result}
                />
            )}

            {appData.current.activeTab === "tasks" && (
                <TaskManager
                    tasks={appData.current.tasks}
                    saveTasks={saveTasks}
                />
            )}

        </div>
    );
}

export default App;
