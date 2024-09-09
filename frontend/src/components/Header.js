import React from 'react';
import '../header.css';  // Assuming you'll have a separate CSS file for this component
import duckLogo from '../assets/icons/duck.png';  // Update the path as needed

const Header = () => {
    const history = useHistory();

    const handleClick = () => {
        history.push('/file-explorer');  // Navigate to file-explorer on click
    };

    return (
        <div className="header" onClick={handleClick}>
            {/* <img src={duckLogo} alt="DUCKS Logo" className="logo" /> */}
            <h1 className="title">DUCKS</h1>
        </div>
    );
};

export default Header;
