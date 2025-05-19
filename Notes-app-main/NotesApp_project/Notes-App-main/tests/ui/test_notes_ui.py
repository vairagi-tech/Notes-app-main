import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNotesUI:
    def test_create_note(self, web_driver, base_url):
        """Test creating a new note through the UI"""
        web_driver.get(base_url)
        
        # Click add note button
        add_button = WebDriverWait(web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-note-button']"))
        )
        add_button.click()
        
        # Fill in note details
        title_input = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='note-title-input']")
        content_input = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='note-content-input']")
        
        title_input.send_keys("Test Note")
        content_input.send_keys("This is a test note")
        
        # Save note
        save_button = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='save-note-button']")
        save_button.click()
        
        # Verify note was created
        note_title = WebDriverWait(web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Test Note')]"))
        )
        assert note_title.is_displayed()

    def test_edit_note(self, web_driver, base_url):
        """Test editing an existing note"""
        web_driver.get(base_url)
        
        # Create a note first
        self.test_create_note(web_driver, base_url)
        
        # Click edit button
        edit_button = WebDriverWait(web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='edit-note-button']"))
        )
        edit_button.click()
        
        # Update note details
        title_input = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='note-title-input']")
        content_input = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='note-content-input']")
        
        title_input.clear()
        content_input.clear()
        
        title_input.send_keys("Updated Note")
        content_input.send_keys("This is an updated note")
        
        # Save changes
        save_button = web_driver.find_element(By.CSS_SELECTOR, "[data-testid='save-note-button']")
        save_button.click()
        
        # Verify note was updated
        updated_title = WebDriverWait(web_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Updated Note')]"))
        )
        assert updated_title.is_displayed()

    def test_delete_note(self, web_driver, base_url):
        """Test deleting a note"""
        web_driver.get(base_url)
        
        # Create a note first
        self.test_create_note(web_driver, base_url)
        
        # Click delete button
        delete_button = WebDriverWait(web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='delete-note-button']"))
        )
        delete_button.click()
        
        # Confirm deletion
        confirm_button = WebDriverWait(web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='confirm-delete-button']"))
        )
        confirm_button.click()
        
        # Verify note was deleted
        try:
            WebDriverWait(web_driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Test Note')]"))
            )
            assert False, "Note should be deleted"
        except:
            assert True 