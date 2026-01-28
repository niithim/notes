/**
 * Dashboard page functionality
 * Handles notes CRUD operations
 */

let notes = [];
let editNoteModal = null;

document.addEventListener('DOMContentLoaded', () => {
    // Check authentication
    checkAuth();

    // Initialize Bootstrap modal
    editNoteModal = new bootstrap.Modal(document.getElementById('editNoteModal'));

    // Load user info
    const userInfo = TokenManager.getUserInfo();
    document.getElementById('userWelcome').textContent = `Welcome, ${userInfo.userName}!`;

    // Event listeners
    document.getElementById('logoutBtn').addEventListener('click', handleLogout);
    document.getElementById('createNoteForm').addEventListener('submit', handleCreateNote);
    document.getElementById('saveEditBtn').addEventListener('click', handleUpdateNote);

    // Load notes
    loadNotes();
});

function handleLogout() {
    TokenManager.removeToken();
    window.location.href = 'index.html';
}

async function loadNotes() {
    try {
        notes = await apiRequest('/notes');
        renderNotes();
    } catch (error) {
        showAlert(error.message || 'Failed to load notes.', 'danger');
        document.getElementById('notesList').innerHTML = '<p class="text-danger text-center">Failed to load notes.</p>';
    }
}

function renderNotes() {
    const notesList = document.getElementById('notesList');

    if (notes.length === 0) {
        notesList.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📝</div>
                <p>No notes yet. Create your first note above!</p>
            </div>
        `;
        return;
    }

    notesList.innerHTML = notes.map(note => `
        <div class="note-card" data-note-id="${note.id}">
            <div class="note-title">${escapeHtml(note.title)}</div>
            <div class="note-content">${escapeHtml(note.content)}</div>
            <div class="note-date">
                Created: ${formatDate(note.created_at)} | 
                Updated: ${formatDate(note.updated_at)}
            </div>
            <div class="note-actions">
                <button class="btn btn-sm btn-primary" onclick="editNote(${note.id})">Edit</button>
                <button class="btn btn-sm btn-danger" onclick="deleteNote(${note.id})">Delete</button>
            </div>
        </div>
    `).join('');
}

async function handleCreateNote(e) {
    e.preventDefault();

    const title = document.getElementById('noteTitle').value;
    const content = document.getElementById('noteContent').value;

    try {
        await apiRequest('/notes', {
            method: 'POST',
            body: JSON.stringify({
                title: title,
                content: content
            })
        });

        // Clear form
        document.getElementById('createNoteForm').reset();

        // Reload notes
        loadNotes();

        showAlert('Note created successfully!', 'success');
    } catch (error) {
        showAlert(error.message || 'Failed to create note.', 'danger');
    }
}

function editNote(noteId) {
    const note = notes.find(n => n.id === noteId);
    if (!note) return;

    document.getElementById('editNoteId').value = note.id;
    document.getElementById('editNoteTitle').value = note.title;
    document.getElementById('editNoteContent').value = note.content;

    editNoteModal.show();
}

async function handleUpdateNote() {
    const noteId = document.getElementById('editNoteId').value;
    const title = document.getElementById('editNoteTitle').value;
    const content = document.getElementById('editNoteContent').value;

    try {
        await apiRequest(`/notes/${noteId}`, {
            method: 'PUT',
            body: JSON.stringify({
                title: title,
                content: content
            })
        });

        editNoteModal.hide();
        loadNotes();
        showAlert('Note updated successfully!', 'success');
    } catch (error) {
        showAlert(error.message || 'Failed to update note.', 'danger');
    }
}

async function deleteNote(noteId) {
    if (!confirm('Are you sure you want to delete this note?')) {
        return;
    }

    try {
        await apiRequest(`/notes/${noteId}`, {
            method: 'DELETE'
        });

        loadNotes();
        showAlert('Note deleted successfully!', 'success');
    } catch (error) {
        showAlert(error.message || 'Failed to delete note.', 'danger');
    }
}

// Utility functions
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
}
