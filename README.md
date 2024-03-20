# Internet Speed Twitter Bot

The Internet Speed Twitter Bot is a Python script designed to automate the process of testing internet speed and tweeting the results to the internet service provider's Twitter account. This bot utilizes Selenium, a web automation tool, to interact with the Speedtest website for measuring internet speed and the Twitter website for posting tweets.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (download from [here](https://sites.google.com/chromium.org/driver/))

## Setup

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/internet-speed-twitter-bot.git
    ```

3. Download the Chrome WebDriver and specify its path in the `CHROME_DRIVER_PATH` variable within the script.

4. Update the `TWITTER_ID` and `TWITTER_PASSWORD` variables in the script with your Twitter credentials.

## Usage

To run the bot, execute the following command:


## Functionality

1. **Testing Internet Speed**: The bot navigates to the Speedtest website, initiates the speed test, and retrieves the download and upload speed results.

2. **Tweeting at Provider**: After obtaining the internet speed results, the bot logs into Twitter, composes a tweet mentioning the internet service provider, and posts the tweet.

## Customization

- Adjust the `PROMISED_DOWN` and `PROMISED_UP` variables to match the promised download and upload speeds according to your internet plan.
- Customize the tweet message to suit your preferences or specific situation.

## Disclaimer

This bot interacts with external websites and social media platforms. Use it responsibly and ensure compliance with the terms of service of the websites being accessed.

**Happy tweeting! 🚀**
