import React from 'react';
import Sidebar from './components/Sidebar';
import FileExplorer from './components/FileExplorer';
import Ponds from './components/Ponds';
import Settings from './components/Settings';
import './styles.css';

const App = () => {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="content">
        {/* Content can be conditionally rendered based on active menu item */}
        <FileExplorer />
        {/* Add Ponds and Settings components as needed */}
      </div>
    </div>
  );
};

export default App;
