import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../fileExplorer.css';

const FileExplorer = () => {
  const [files, setFiles] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/files');
        setFiles(response.data);
        setError(null);
      } catch (error) {
        console.error('Error fetching files:', error.response ? error.response.data : error.message);
        setError(error.response ? error.response.data.error : error.message);
      }
    };

    fetchFiles();
  }, []);

  return (
    <div className="file-explorer">
      <h2>File Explorer</h2>
      {error && <p className="error-message">{error}</p>}
      {files.length > 0 ? (
        <ul>
          {files.map((file) => (
            <li key={file.id}>
              <a href={file.url} download={file.name}>{file.name}</a>  {/* Enable file downloading */}
            </li>
          ))}
        </ul>
      ) : (
        <p>No files found.</p>
      )}
    </div>
  );
};

export default FileExplorer;
