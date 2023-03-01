import {useState } from 'react'
import axios from 'axios'
const Home  = () => {
    
    const [context , setContext ] = useState('')
    const [question , setQ] = useState('')
    const [answer , setAnswer] = useState('')
    const handleContextChange = (e) => { 
        const context = e.target.value 
        setContext(context)
        console.log(context)
    } 
    const handleQuestionChange = (e) => {
        const question  = e.target.value 
        setQ(question) 
        console.log(question)
    }
    const handleClick = () => {
        // console.log('clicked')
        const data = {
            'context' : context , 
            'question' : question 
        }
        axios.post('http://localhost:8000/predict/' , data)
        .then(res => setAnswer(res.data))
    }
    
    return (  
        <div> 
            <h2>Question Answering</h2>
            <p>This app can answer your question depend on a context </p>
            <div>
                <textarea  value={context}  onChange ={handleContextChange} placeholder='context' /> <br></br>
                <input value={question} onChange = {handleQuestionChange} placeholder ='question' />  
                <button type='submit' onClick={handleClick} >submit</button>
            </div>
            {answer && <p>{answer}</p>}
        </div>
    );
}

export default Home ;