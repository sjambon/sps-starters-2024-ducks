import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Update to your Flask API URL

export const getFiles = async () => {
    try {
        return await axios.get(`${API_URL}/files`);
    } catch (error) {
        console.error('Error fetching files:', error.response.data);
        throw error;
    }
};

export const getFolders = async () => {
    try {
        return await axios.get(`${API_URL}/folders`);
    } catch (error) {
        console.error('Error fetching folders:', error.response.data);
        throw error;
    }
};

export const getTags = async () => {
    try {
        return await axios.get(`${API_URL}/tags`);
    } catch (error) {
        console.error('Error fetching tags:', error.response.data);
        throw error;
    }
};

export const uploadFile = async (file) => {
    try {
        const formData = new FormData();
        formData.append('file', file);

        return await axios.post(`${API_URL}/files/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
    } catch (error) {
        console.error('Error uploading file:', error.response.data);
        throw error;
    }
};