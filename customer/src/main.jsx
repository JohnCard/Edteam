import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import App from './App.jsx'
import Menu from './components/Menu.jsx'
import FormCourse from './components/Form'
import { Toaster } from 'react-hot-toast'

ReactDOM.createRoot(document.getElementById('root')).render(
        <BrowserRouter>
            <Routes>
                {/* main routes */}
                <Route path='/' element={<Menu />} >
                    {/* intex link */}
                    <Route index element={<App />} />
                    {/* form link */}
                    <Route path='/Form' element={<FormCourse />} />
                    {/* update link */}
                    <Route path='/Form/:id' element={<FormCourse />} />
                </Route>
            </Routes>
            <Toaster />
        </BrowserRouter>
)
