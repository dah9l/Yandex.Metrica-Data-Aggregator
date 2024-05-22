# Yandex.Metrica Data Aggregator

## The Yandex.Metrica Data Aggregator is a Python script that automatically collects data from various Yandex.Metrica API sources and aggregates them into a unified SQLite database.

### Features
* Retrieves data from Yandex.Metrica API using an API key
* Collects metrics such as visits, pageviews, bounce rate, and average visit duration
* Stores the collected data in a SQLite database table named "metrika_data"
* Creates the "metrika_data" table if it doesn't exist

### Prerequisites
* Python 3.x installed
* Required Python libraries: requests, sqlite3, json
* A valid Yandex.Metrica API key
* The counter ID for which you want to collect data

### Installation
1. Clone or download the repository containing the script.
2. Install the required Python libraries if not already installed.

### Usage
1. Open the script in a text editor.
2. Replace `YOUR_API_KEY` with your actual Yandex.Metrica API key.
3. Replace `YOUR_COUNTER_ID` with the counter ID for which you want to collect data.
4. Save the changes to the script.
5. Run the script using Python:
```bash
python yandex_metrica_aggregator.py
```
6. The script will collect the data from Yandex.Metrica API and store it in the SQLite database file named “metrika_data.db”.

### Database Schema
The script creates a table named “metrika_data” in the SQLite database with the following columns:

* date: Date of the data (type: DATE)
* visits: Number of visits (type: INTEGER)
* pageviews: Number of pageviews (type: INTEGER)
* bounce_rate: Bounce rate (type: REAL)
* avg_visit_duration: Average visit duration (type: REAL)

### Example
```bash
CREATE TABLE metrika_data (
    date DATE,
    visits INTEGER,
    pageviews INTEGER,
    bounce_rate REAL,
    avg_visit_duration REAL
);
```

### Contributing
If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request.

### License
This project is licensed under the MIT License.
