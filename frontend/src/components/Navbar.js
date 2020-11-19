import React, { useState, useEffect } from 'react';
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [click, setClick] = useState(false);

  const closeMobileMenu = () => setClick(false);


  return (
    <>
      <nav className='navbar'>
        <div className='navbar-container'>
          <Link to='/' className='navbar-logo' onClick={closeMobileMenu}>
            TARUJA
            <i class='fab fa-typo3' />
          </Link>
          <div className='nav-button'>
            <Button buttonStyle='btn--outline'>SIGN UP</Button>
          </div>
        
        </div>
        <br />
        
      </nav>
      <nav className='searchbar-nav'>
          <div className='searchbar-container'>
            <input className='search-bar' placeholder='Search...' />
            </div>
        </nav>
    </>
  );
}

export default Navbar;