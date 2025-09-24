# League Match Stats

This is a simple project that helped me expand my knowledge of **Python**, **API calls**, and **Flask**.

## Technologies Used
- **Python**
- **Flask**
- **HTML**
- **Riot Games API**

## How it works
- Uses Riot Games' North America API with a developer API key (not provided in here for security purposes).
- Grabs the last 5 matches a player has played in **League of Legends** (only 5v5 matches).
- Includes a website where user enters their **Username** and **Tag**.
- Website sends data to a **Python backend (FLask)**, and shows results in console

## Future Improvements
- Add database integration to stroe match history (MySQl).
- Create data charts (Win rate per champion).
- Add css to make it look nicer.
- Make it accessible outside of loclhost.

## Getting Started
# Prerequisites
- Riot Developer Portal API key (You can get a 24-hour one by signing up on this website "https://developer.riotgames.com/")
- Python 3.x
  
1. Clone this repository.
2. Make a .env file or a variable named "riot_api_key"
3. Install dependencies:
   ```bash
   pip install Flask
4. Run the python project, and then run the html files
5. Open http://localhost:5000 in your browser, and viola!
