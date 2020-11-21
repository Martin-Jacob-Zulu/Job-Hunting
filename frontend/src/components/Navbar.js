import React, { useState, useEffect } from 'react';
import { Button } from './Button';
import { Link } from 'react-router-dom';
import './Navbar.css';
import { Select } from './Select';
import Category from './Category';

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
          
          <div className='searchbar-container'>
            <Select selectStyle='nav--select--outline '>
                <optgroup className='select-group' label='Categories'>
                    <option className='select-item'>All</option>
                    <option className='select-item'>Jobs</option>
                    <option className='select-item'>Business</option>
                    <option className='select-item'>Educational</option>
                    <option className='select-item'>Style</option>
                    <option className='select-item'>Design</option>
                    <option className='select-item'>Weather</option>
                    <option className='select-item'>Politics</option>
                </optgroup>
            </Select>
            
            <input className='nav-searchbar' placeholder='Search...' />
            
            
            <Button buttonStyle='nav--btn--search'>
                <i className='fas fa-search' />
            </Button>
            </div>
          <div className='nav-button'>
            <Button buttonStyle='btn--outline'>SIGN UP</Button>
            </div>
        
        </div>
        <br />
        
      </nav>
      <nav className='searchbar-nav'>
          <div className='searchbar-categories'>
            <Select selectStyle='select--outline'>
                <optgroup className='select-group' label='Categories'>
                    <option className='select-item'>All</option>
                    <option className='select-item'>Jobs</option>
                    <option className='select-item'>Business</option>
                    <option className='select-item'>Educational</option>
                    <option className='select-item'>Style</option>
                    <option className='select-item'>Design</option>
                    <option className='select-item'>Weather</option>
                    <option className='select-item'>Politics</option>
                </optgroup>
            </Select>
            </div>
          <div className='searchbar-container'>
            <input className='search-bar' placeholder='Search...' />
            </div>
          <div className='searchbar-button'>
            <Button buttonStyle='btn--search'>
                <i className='fas fa-search' />
            </Button>
            </div>
        </nav>
        <nav className='category-nav'>
            <div className='category-container'>
                {/* <Category></Category> */}
            </div>
        </nav>
    </>
  );
}

export default Navbar;