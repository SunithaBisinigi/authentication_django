// ToDoList.js
import React, { useState, useEffect } from 'react';
import ToDoItem from './ToDoItem';

function ToDoList() {
  const [items, setItems] = useState([]);
  const [newItemText, setNewItemText] = useState('');

  useEffect(() => {
    // Fetch to-do items from your Django API endpoint
    // and update the 'items' state
  }, []);

  const handleCreateItem = () => {
    // Send a POST request to create a new to-do item in Django
    // and update the 'items' state
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Add a new to-do"
        value={newItemText}
        onChange={(e) => setNewItemText(e.target.value)}
      />
      <button onClick={handleCreateItem}>Add</button>
      <ul>
        {items.map((item) => (
          <ToDoItem key={item.id} item={item} />
        ))}
      </ul>
    </div>
  );
}

export default ToDoList;
