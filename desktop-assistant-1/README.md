# Desktop Assistant

This project is a desktop assistant application built using Python and Tkinter. It provides various features including time display, traffic information, scheduling, currency conversion, and web searching.

## Features

- **Time Display**: Shows the current time and date.
- **Traffic Information**: Retrieves and displays real-time traffic data.
- **Scheduling**: Allows users to manage their schedules by adding, removing, and viewing tasks and events.
- **Currency Conversion**: Provides functionality for converting currencies and fetching exchange rates.
- **Web Searching**: Enables searches on Baidu and Bing.
- **Web Scraping**: Allows users to scrape data from specified websites.

## Project Structure

```
desktop-assistant
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui
│   │   └── main_window.py     # Main user interface
│   ├── services
│   │   ├── time_service.py    # Time service
│   │   ├── traffic_service.py  # Traffic service
│   │   ├── schedule_service.py # Schedule service
│   │   ├── currency_service.py # Currency service
│   │   ├── search_service.py   # Search service
│   │   └── web_scraper.py     # Web scraping service
│   └── utils
│       └── helper.py          # Utility functions
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/desktop-assistant.git
   ```
2. Navigate to the project directory:
   ```
   cd desktop-assistant
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.