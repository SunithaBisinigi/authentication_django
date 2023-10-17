// ToDoItem.js
import React, { useState } from 'react';

function ToDoItem({ item }) {
  const [isEditing, setIsEditing] = useState(false);
  const [updatedText, setUpdatedText] = useState(item.text);

  const handleUpdate = () => {
    // Send a PUT request to update the item's text
    // and set isEditing to false
  };

  const handleDelete = () => {
    // Send a DELETE request to remove the item from Django
  };

  return (
    <li>
      {isEditing ? (
        <>
          <input value={updatedText} onChange={(e) => setUpdatedText(e.target.value)} />
          <button onClick={handleUpdate}>Save</button>
        </>
      ) : (
        <>
          {item.text}
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </>
      )}
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
}

export default ToDoItem;
