import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../ponds.css';

const Ponds = () => {
  const [ponds, setPonds] = useState([]);

  useEffect(() => {
    const fetchPonds = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/ponds');
        setPonds(response.data);
      } catch (error) {
        console.error('Error fetching ponds:', error);
      }
    };

    fetchPonds();
  }, []);

  return (
    <div className="pond-list">
      <h2>Ponds</h2>
      <ul>
        {ponds.map((pond) => (
          <li key={pond.id}>{pond.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Ponds;
