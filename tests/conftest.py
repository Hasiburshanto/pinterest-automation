import pytest
import time

@pytest.fixture(scope="function")
def pinterest(request):
    pinterest = PinterestAutomation()
    pinterest.open_pinterest()
    
    # Adding a finalizer to take a screenshot after each test case
    def teardown():
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"screenshot_{request.node.name}_{timestamp}.png"
        pinterest.driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved as {screenshot_filename}")
        pinterest.quit()

    request.addfinalizer(teardown)
    return pinterest
