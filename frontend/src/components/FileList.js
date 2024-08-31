import React, { useEffect, useState } from 'react';
import { getFiles } from '../api';

const FileList = () => {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchFiles = async () => {
      const response = await getFiles();
      setFiles(response.data);
    };
    fetchFiles();
  }, []);

  return (
    <div className="file-list">
      <h2>Files</h2>
      <ul>
        {files.map(file => (
          <li key={file.id}>{file.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default FileList;
