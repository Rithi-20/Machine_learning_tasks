import {useRef, useEffect} from 'react';
// console.log(1);

function Calculator({calculate,result}){
    // console.log(2);
    const firstnum=useRef(null);
    const secondnum=useRef(null);
    const operator=useRef(null);
    // useEffect(()=> console.log(3),[]);

    const handleCalculate=()=> {
        const num1=firstnum.current.value;
        const num2=secondnum.current.value;

        if(num1.trim()==="" || num2.trim()===""){
            alert("Please enter both numbers");
            return;
        }

        const a=Number(num1);
        const b=Number(num2);
        calculate(a,b,operator.current.value);

    };

    return(
        <div className="card">
            {/* {console.log(4)} */}
            <h2>Calculator</h2>

            <input type="number" placeholder="Enter first number" ref={firstnum}/>

            <input type="number" placeholder="Enter second number" ref={secondnum}/>

            <select ref={operator}>
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>

           </select>


           <button onClick={handleCalculate}>Calculate</button>
           <div className="result">
                <h3>Result: {result ?? "Not calculated yet"}</h3>
            </div>
        </div>
    )
}

export default Calculator;



