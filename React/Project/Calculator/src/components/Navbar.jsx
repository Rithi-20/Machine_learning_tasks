
function Navbar({ activeTab, changeTab }) {

    return (
        <nav className="navbar">

            <button
                className={activeTab === "calculator" ? "active" : ""}
                onClick={() => changeTab("calculator")}
            >
                Calculator
            </button>

            <button
                className={activeTab === "tasks" ? "active" : ""}
                onClick={() => changeTab("tasks")}
            >
                Task Manager
            </button>

        </nav>
    );
}

export default Navbar;
