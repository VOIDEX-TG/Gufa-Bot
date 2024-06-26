from telethon import TelegramClient, events

# Configure the Telegram client
api_id = "599204"
api_hash = "1c40c54693e2cdbe590a152ed1bd5f"
bot_token = "704444323:AAGSsD9LOw3_BGqbgjy2Tuvoiy2mTOsCo"

# Initialize the Telegram client
client = TelegramClient("my_bot", api_id, api_hash).start(bot_token=bot_token)

# Define the channel link
channel_link = "https://t.me/wijcj27"

# Global variable to keep track of the current video index
current_video_index = 0

# Function to get videos from channel
# Function to get videos from channel
def get_channel_videos():
    # List of video URLs
    video_urls = [
                  "https://t.me/wijcj27/3"
                  "https://t.me/wijcj27/9"
                 ]
    return video_urls


# Event handler for the "/start" command
@client.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    await event.respond("Press the button to get a video from the channel.")

# Event handler for "/get_video" command

# ... (get_channel_videos function)

@client.on(events.NewMessage(pattern='/get_video'))
async def get_video_command(event):
    global current_video_index
    videos = get_channel_videos()
    if current_video_index < len(videos):
        video_url = videos[current_video_index]
        await event.respond(file=video_url)
        current_video_index += 1
        if current_video_index >= len(videos):  # Check if we've reached the end
            current_video_index = 0  # Reset the index

# ... (rest of your code)

# ... (rest of your imports and setup)

# ... (get_channel_videos function)

# ... (rest of your code)


# Start the client
client.run_until_disconnected()