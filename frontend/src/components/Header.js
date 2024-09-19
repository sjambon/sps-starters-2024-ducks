import React from 'react';
import '../header.css';
import duckLogo from '../assets/icons/duck.png';
import { useNavigate } from 'react-router-dom';

const Header = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/file-explorer');
    };

    return (
        <div className="header" onClick={handleClick}>
            <h1 className="title">DUCKS</h1>
        </div>
    );
};

export default Header;
