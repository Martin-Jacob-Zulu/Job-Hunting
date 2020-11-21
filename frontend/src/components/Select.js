import React from 'react';
import './Select.css';


const STYLES = ['select--primary', 'select--outline', 'select--category', 'nav--select--outline ']

const SIZES = ['select--medium', 'select--large']


export const Select = ({
    children, type, selectStyle, selectSize
}) => {
    const checkSelectStyle = STYLES.includes(selectStyle) ? selectStyle : STYLES[0];

    const checkSelectSize = SIZES.includes(selectSize) ? selectSize : SIZES[0];

    return (
        <select className={`select ${checkSelectStyle} ${checkSelectSize}`}>
            {children}
        </select>
    )
}