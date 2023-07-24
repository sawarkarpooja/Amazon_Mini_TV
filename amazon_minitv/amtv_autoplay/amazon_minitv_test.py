import time          #Import Time module
import pytest        #import pytest module for Assertions
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions
from selenium import webdriver   #Importing the 'webdriver' module from the 'selenium' package.
from selenium.webdriver.common.by import By  #By is used to locate elements on a webpage while using Selenium WebDriver.

# Task 1: Opening Amazon MiniTV
@pytest.fixture(scope="module")  # Pytest fixture to set up and provide resources at the module level.
def driver():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) ## The 'implicitly_wait' method instructs the WebDriver to wait for a specified time
    yield driver
    # After all the tests are done , close the browser
    driver.quit()

def test_open_amazon_minitv(driver):
    # Navigate to the Amazon MiniTV website
    driver.get("https://www.amazon.in/minitv?mtv_pt=external&refMarker=AVOD_gs_mw_BRND_EDU_GS_TXT_AD2&gclid=Cj0KCQjwn_OlBhDhARIsAG2y6zMjx5_tiCtwXYJzbLkhOATL2zxOe-EHL2b6dAx12ouiOllRL4S07ysaAvtcEALw_wcB")
    # Wait for the page to load
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)
    # Check if the Amazon MiniTV page is opened
    assert "Watch Free Web Series & Short Films Online | Amazon miniTV" in driver.title
def test_select_series(driver):
    # Find and click on the "Highway Love" series
    series_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ThumbnailCard_thumbnailImage__4GhPv"))
    )
    series_link.click()  # Click on the series link
    # Wait for the series details page to load
    time.sleep(3)
    # Check if the series details page is opened
    assert "Highway Love' in 'Watch Hip Hop India Season 1 Episode 1 for Free | Amazon miniTV" in driver.title

try:
    # Step 1: Open the Amazon MiniTV website
    driver.get("https://www.amazon.in/minitv?mtv_pt=external&refMarker=AVOD_gs_mw_BRND_EDU_GS_TXT_AD2&gclid=Cj0KCQjwn_OlBhDhARIsAG2y6zMjx5_tiCtwXYJzbLkhOATL2zxOe-EHL2b6dAx12ouiOllRL4S07ysaAvtcEALw_wcB")

    # Step 2: Find and click on the "Highway Love" series
    series_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Highway Love' in 'Watch Hip Hop India Season 1 Episode 1 for Free | Amazon miniTV"))
    )
    series_link.click()

    # Wait for the series details page to load
    time.sleep(3)

    # Verify if the series details page is opened
    if "Highway Love" in driver.title:
        print("Series 'Highway Love' opened successfully.")
    else:
        print("Failed to open the series 'Highway Love'.")

except Exception as e:
    print("An error occurred:", str(e))


def is_video_playing(driver):
    try:
        video_player_title = driver.find_element(By.CLASS_NAME, "video-player-title")
        return video_player_title.is_displayed()
    except NoSuchElementException:
        return False

# Test to count the number of episodes in the "Highway Love" series
def test_count_episodes(driver):
    # Open the "Highway Love" series details page
    driver.get("https://www.amazon.in/minitv/tp/f77d9c82-9f7f-427c-923a-d1cd12d72e3e")

    # Wait for the series details page to load
    time.sleep(3)

    # Find all the season links on the series details page
    seasons = driver.find_elements(By.CLASS_NAME, "rmc-tabs-tab-bar-underline")
    total_episodes = 0

    ## Iterate through each season
    for season in seasons:
        season.click()
        # Wait for the season details page to load
        time.sleep(3)
        # Find all the episodes in the current season
        episodes = driver.find_elements(By.CLASS_NAME, "ThumbnailCard_playIconContainer__IkFPt")
        total_episodes += len(episodes)

    # Verify that the number of episodes matches the expected count
    expected_total_episodes = 8
    assert total_episodes == expected_total_episodes

# Test case to play the first episode of each season
def test_play_first_episode(driver):
    # Find all the season links on the series details page
    seasons = driver.find_elements(By.CLASS_NAME, "seasonListItem")

    # Iterate through each season
    for season in seasons:
        season.click()
        # Wait for the season details page to load
        time.sleep(3)
        # Find and click on the first episode to start playing it
        first_episode_link = driver.find_element(By.CLASS_NAME, "ThumbnailCard_playIconContainer__IkFPt")
        first_episode_link.click()
        # Wait for the video to start playing (you can adjust the delay as needed)
        time.sleep(5)
        # Verify that the video is playing
        assert is_video_playing(driver)




def is_video_playing(driver):
    video_player_title = driver.find_element(By.CLASS_NAME, "video-player-title")
    return video_player_title.is_displayed()