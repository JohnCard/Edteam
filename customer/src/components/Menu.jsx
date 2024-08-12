import React from 'react'
import { NavLink, Outlet } from "react-router-dom"

function Menu() {
  return (
    <>
    <nav>
        <ul>
          {/* NavLink was designed to work within main menu and Link was designed to work into BrowseRouter */}
            {/* go to the init */}
            <li><NavLink to='/' >Init</NavLink></li>
            {/* go to create a new course */}
            <li><NavLink to='/Form' > Form</NavLink></li>
            <Outlet />
        </ul>
    </nav>
    </>
  )
}

export default Menu