# Telegram Game Bot

A Telegram bot that provides information about free games.

## Features

- Fetches game information from a JSON file.
- Responds to the `/new` command to display the list of games.
- Displays game name, store, duration, and URL.

## Prerequisites

- Python 3.6 or higher
- Required Python packages can be installed using `pip`. Use the following command:



## Usage

1. Clone the repository:



2. Create a virtual environment (optional):



3. Install the required packages:


4. Create a JSON file containing game information:
- Create a file named `week1.json` in the project directory.
- Add game information to the JSON file in the specified format:
  ```json
  {
    "games": [
      {
        "name": "Game 1",
        "store": "Store A",
        "duration": "2 weeks",
        "url": "https://example.com/game1"
      },
      {
        "name": "Game 2",
        "store": "Store B",
        "duration": "1 month",
        "url": "https://example.com/game2"
      }
    ]
  }
  ```

5. Set up a Telegram bot:
- Create a new bot using BotFather on Telegram.
- Obtain your bot token.

6. Set the environment variable for the bot token:
- Rename the `.env.example` file to `.env`.
- Replace `YOUR_TOKEN_HERE` with your actual bot token in the `.env` file.

7. Start the bot: python main.py or py main.py



8. Open your Telegram app and search for your bot.
- Start a conversation with the bot.
- Use the `/new` command to fetch and display the list of games.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please feel free to submit a pull request.




