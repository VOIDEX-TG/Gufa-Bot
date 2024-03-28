**Telegram Video Scraper**

![Powered By Voidex](https://telegra.ph/file/f0b21cd8808d4fc97eb62.png)


**Description:**
This script utilizes the Telethon library to scrape videos from a Telegram channel and send them to users upon request. It allows users to request videos from the channel through commands and buttons.

**Requirements:**
- Python 3.x
- Telethon library

**Installation:**
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install the Telethon library by running `pip install telethon` in your terminal.

**Usage:**
1. Clone or download the script to your local machine.
2. Replace the placeholder values for `api_id`, `api_hash`, and `bot_token` with your own Telegram API credentials.
3. Modify the `channel_link` variable to point to the Telegram channel from which you want to scrape videos.
4. Run the script using `python bot.py`.
5. Start the bot in your Telegram client by sending the `/start` command.

**Commands:**
- `/start`: Initiates the bot and displays a prompt to the user.
- `/get_video`: Requests a video from the channel. Users can click the provided button to receive the next video available.

**Important Notes:**
- Ensure that your Telegram API credentials (`api_id`, `api_hash`, and `bot_token`) are kept secure and not shared publicly.
- Make sure the Telegram channel you're scraping videos from allows bot access and sharing of its content.
- This script assumes a single channel link and a predefined list of video URLs. Modify the `get_channel_videos()` function to dynamically fetch videos from the channel if needed.

**Author:**
[HexorXd](https://t.me/Sher_e_Purvanchal)

**Contact:**
[Telegram](https://t.me/VoidexTg)
