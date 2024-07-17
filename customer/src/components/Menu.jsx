import React from 'react'
import { NavLink, Outlet } from "react-router-dom"

function Menu() {
  return (
    <>
    <nav>
        <ul>
          {/* NavLink esta diseñado para funcionar dentro del menu principal y Link esta diseñdo para funcionar dentro del BrowseRouter */}
            <li><NavLink to='/' >Init</NavLink></li>
            <li><NavLink to='/Form' > Form</NavLink></li>
            <Outlet />
        </ul>
    </nav>
    </>
  )
}

export default Menu