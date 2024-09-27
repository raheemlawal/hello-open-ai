import { useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {

  const [openAIResponse, setOpenAIResponse] = useState("")

  async function sayHelloToOpenAI()
  {
    try{
      await axios.post('http://127.0.0.1:8000/hello')
      .then(response => {
        setOpenAIResponse(response.data.content);
      })
    }
    catch(e){
      console.log(e)
    }
  }

  return (
    <>
      <div>
        <h1>Hello OpenAI</h1>
        <button className='bg-lime-400 px-2 py-4 rounded w-96' onClick={sayHelloToOpenAI}>Say Hello</button>
        <h1 className='text-white mt-2 text-md'>{openAIResponse}</h1>
      </div>
    </>
  )
}

export default App
