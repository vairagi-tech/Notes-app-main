import pytest
import json

def test_create_note(api_client, api_url):
    """Test creating a new note"""
    note_data = {
        "title": "Test Note",
        "content": "This is a test note"
    }
    response = api_client.post(f"{api_url}/api/notes", json=note_data)
    assert response.status_code == 201
    assert response.json()["title"] == note_data["title"]
    assert response.json()["content"] == note_data["content"]

def test_get_notes(api_client, api_url):
    """Test retrieving all notes"""
    response = api_client.get(f"{api_url}/api/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_note_by_id(api_client, api_url):
    """Test retrieving a specific note"""
    # First create a note
    note_data = {
        "title": "Test Note",
        "content": "This is a test note"
    }
    create_response = api_client.post(f"{api_url}/api/notes", json=note_data)
    note_id = create_response.json()["id"]
    
    # Then get the note
    response = api_client.get(f"{api_url}/api/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id

def test_update_note(api_client, api_url):
    """Test updating a note"""
    # First create a note
    note_data = {
        "title": "Test Note",
        "content": "This is a test note"
    }
    create_response = api_client.post(f"{api_url}/api/notes", json=note_data)
    note_id = create_response.json()["id"]
    
    # Update the note
    update_data = {
        "title": "Updated Note",
        "content": "This is an updated note"
    }
    response = api_client.put(f"{api_url}/api/notes/{note_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == update_data["title"]
    assert response.json()["content"] == update_data["content"]

def test_delete_note(api_client, api_url):
    """Test deleting a note"""
    # First create a note
    note_data = {
        "title": "Test Note",
        "content": "This is a test note"
    }
    create_response = api_client.post(f"{api_url}/api/notes", json=note_data)
    note_id = create_response.json()["id"]
    
    # Delete the note
    response = api_client.delete(f"{api_url}/api/notes/{note_id}")
    assert response.status_code == 204
    
    # Verify note is deleted
    get_response = api_client.get(f"{api_url}/api/notes/{note_id}")
    assert get_response.status_code == 404 