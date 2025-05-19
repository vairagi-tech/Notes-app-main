import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNotesMobile:
    @pytest.fixture(scope="function")
    def mobile_driver(self):
        """Fixture to create and manage Appium WebDriver instance"""
        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.notesapp',
            'appActivity': 'com.notesapp.MainActivity',
            'noReset': True
        }
        
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_create_note_mobile(self, mobile_driver):
        """Test creating a new note on mobile"""
        # Click add note button
        add_button = WebDriverWait(mobile_driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.notesapp:id/add_note_button"))
        )
        add_button.click()
        
        # Fill in note details
        title_input = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/note_title_input")
        content_input = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/note_content_input")
        
        title_input.send_keys("Mobile Test Note")
        content_input.send_keys("This is a test note from mobile")
        
        # Save note
        save_button = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/save_note_button")
        save_button.click()
        
        # Verify note was created
        note_title = WebDriverWait(mobile_driver, 10).until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Mobile Test Note']"))
        )
        assert note_title.is_displayed()

    def test_edit_note_mobile(self, mobile_driver):
        """Test editing a note on mobile"""
        # Create a note first
        self.test_create_note_mobile(mobile_driver)
        
        # Click edit button
        edit_button = WebDriverWait(mobile_driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.notesapp:id/edit_note_button"))
        )
        edit_button.click()
        
        # Update note details
        title_input = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/note_title_input")
        content_input = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/note_content_input")
        
        title_input.clear()
        content_input.clear()
        
        title_input.send_keys("Updated Mobile Note")
        content_input.send_keys("This is an updated mobile note")
        
        # Save changes
        save_button = mobile_driver.find_element(MobileBy.ID, "com.notesapp:id/save_note_button")
        save_button.click()
        
        # Verify note was updated
        updated_title = WebDriverWait(mobile_driver, 10).until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Updated Mobile Note']"))
        )
        assert updated_title.is_displayed()

    def test_delete_note_mobile(self, mobile_driver):
        """Test deleting a note on mobile"""
        # Create a note first
        self.test_create_note_mobile(mobile_driver)
        
        # Click delete button
        delete_button = WebDriverWait(mobile_driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.notesapp:id/delete_note_button"))
        )
        delete_button.click()
        
        # Confirm deletion
        confirm_button = WebDriverWait(mobile_driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.notesapp:id/confirm_delete_button"))
        )
        confirm_button.click()
        
        # Verify note was deleted
        try:
            WebDriverWait(mobile_driver, 5).until(
                EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Mobile Test Note']"))
            )
            assert False, "Note should be deleted"
        except:
            assert True 