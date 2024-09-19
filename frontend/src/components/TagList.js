import React, { useEffect, useState } from 'react';
import { getTags } from '../api';

const TagList = () => {
  const [tags, setTags] = useState([]);

  useEffect(() => {
    const fetchTags = async () => {
      const response = await getTags();
      setTags(response.data);
    };
    fetchTags();
  }, []);

  return (
    <div className="tag-list">
      <h2>Tags</h2>
      <ul>
        {tags.map(tag => (
          <li key={tag.id}>{tag.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default TagList;