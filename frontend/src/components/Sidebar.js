import React from 'react';
import '../sidebar.css';
import UploadButton from './UploadButton';
import AccountIcon from './AccountIcon';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <UploadButton />
        <AccountIcon />
      </div>
      <nav className="menu">
        <a href="#file-explorer">File Explorer</a>
        <a href="#ponds">Ponds</a>
      </nav>
      <div className="sidebar-footer">
        <a href="#settings">Settings</a>
      </div>
    </div>
  );
};

export default Sidebar;