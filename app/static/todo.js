document.addEventListener('DOMContentLoaded', function () {
    const todoList = document.getElementById('todo-list');
    const newItemInput = document.getElementById('new-item-input');
    const addItemButton = document.getElementById('add-item-button');

    addItemButton.addEventListener('click', () => {
        const newItemTitle = newItemInput.value;
        if (newItemTitle) {
            const li = document.createElement('li');
            li.innerHTML = `
                    <span class="item-title">${newItemTitle}</span>
                    <button class="edit-button">Edit</button>
                    <button class="delete-button">Delete</button>
                    <input class="edit-input" type="text" value="${newItemTitle}">
                    <button class="save-button" style="display: none;">Save</button>
                    <button class="cancel-button" style="display: none;">Cancel</button>
                `;
            todoList.querySelector('ul').appendChild(li);
            newItemInput.value = '';
        }
    });

    todoList.addEventListener('click', (e) => {
        if (e.target.classList.contains('edit-button')) {
            toggleEdit(e.target.parentElement);
        } else if (e.target.classList.contains('save-button')) {
            saveEdit(e.target.parentElement);
        } else if (e.target.classList.contains('cancel-button')) {
            cancelEdit(e.target.parentElement);
        } else if (e.target.classList.contains('delete-button')) {
            deleteItem(e.target.parentElement);
        }
    });

    function toggleEdit(item) {
        const title = item.querySelector('.item-title');
        const editInput = item.querySelector('.edit-input');
        const saveButton = item.querySelector('.save-button');
        const cancelButton = item.querySelector('.cancel-button');

        title.style.display = 'none';
        editInput.style.display = 'inline';
        saveButton.style.display = 'inline';
        cancelButton.style.display = 'inline';
    }

    function saveEdit(item) {
        const title = item.querySelector('.item-title');
        const editInput = item.querySelector('.edit-input');
        const saveButton = item.querySelector('.save-button');
        const cancelButton = item.querySelector('.cancel-button');

        title.textContent = editInput.value;
        title.style.display = 'inline';
        editInput.style.display = 'none';
        saveButton.style.display = 'none';
        cancelButton.style.display = 'none';
    }

    function cancelEdit(item) {
        const title = item.querySelector('.item-title');
        const editInput = item.querySelector('.edit-input');
        const saveButton = item.querySelector('.save-button');
        const cancelButton = item.querySelector('.cancel-button');

        editInput.value = title.textContent;
        title.style.display = 'inline';
        editInput.style.display = 'none';
        saveButton.style.display = 'none';
        cancelButton.style.display = 'none';
    }

    function deleteItem(item) {
        item.remove();
        // Optionally, you can send an AJAX request to delete the item from the server.
        // Implement server-side logic to delete the item.
    }
})