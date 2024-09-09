import React from 'react';
import Header from './components/Header';  // Import the Header component
import Sidebar from './components/Sidebar';  // Assuming you have a Sidebar component
import FileExplorer from './components/FileExplorer';  // Assuming this is your file explorer component
import './styles.css';

function App() {
  return (
    <div className="App">
      <Header />  {/* Add the header at the top */}
      <div className="content">
        <Sidebar />
        <FileExplorer />
      </div>
    </div>
  );
}

export default App;
