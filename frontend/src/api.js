import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Update to your Flask API URL

export const getUsers = () => axios.get(`${API_URL}/auth/users`);
export const getFiles = () => axios.get(`${API_URL}/files`);
export const getFolders = () => axios.get(`${API_URL}/folders`);
export const getTags = () => axios.get(`${API_URL}/tags`);
