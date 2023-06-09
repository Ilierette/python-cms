import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    //getEvents()
    //getSocialMedia()
    //getWishList()
    //getRecomendations()
  }, [])

  const getEvents = async () => {
    const response = await fetch(`${import.meta.env.VITE_API}/events/`)
    const jsonData = await response.json();
    console.log(jsonData);
  }

  const getSocialMedia = async () => {
    const response = await fetch(`${import.meta.env.VITE_API}/social-links/`)
    const jsonData = await response.json();
    console.log(jsonData);
  }

  const getWishList = async () => {
    const response = await fetch(`${import.meta.env.VITE_API}/wishlist/`)
    const jsonData = await response.json();
    console.log(jsonData);
  }

  const getRecomendations = async () => {
    const response = await fetch(`${import.meta.env.VITE_API}/recomendation-list/`)
    const jsonData = await response.json();
    console.log(jsonData);
  }

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
