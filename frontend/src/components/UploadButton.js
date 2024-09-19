import React, { useRef } from 'react';
import axios from 'axios';
import '../uploadButton.css';

const UploadButton = () => {
  const fileInputRef = useRef(null);

  const handleFileUpload = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      console.log('File selected:', file);

      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await axios.post('http://localhost:5000/api/files/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('File uploaded successfully:', response.data);
        window.location.reload(); // Reload the page after successful upload
      } catch (error) {
        console.error('Error uploading file:', error.response ? error.response.data : error.message);
      }
    }
  };

  return (
    <div>
      <button className="upload-button" onClick={handleFileUpload}>Upload</button>
      <input
        type="file"
        ref={fileInputRef}
        style={{ display: 'none' }}
        onChange={handleFileChange}
      />
    </div>
  );
};

export default UploadButton;
