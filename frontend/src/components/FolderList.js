import React, { useEffect, useState } from 'react';
import { getFolders } from '../api';

const FolderList = () => {
  const [folders, setFolders] = useState([]);

  useEffect(() => {
    const fetchFolders = async () => {
      const response = await getFolders();
      setFolders(response.data);
    };
    fetchFolders();
  }, []);

  return (
    <div className="folder-list">
      <h2>Folders</h2>
      <ul>
        {folders.map(folder => (
          <li key={folder.id}>{folder.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default FolderList;