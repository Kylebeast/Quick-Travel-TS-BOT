# TeamSpeak Quick Travel Bot

This is a Python bot for TeamSpeak that automatically moves users between specific channels based on their channel IDs.

## Requirements
- Python 3.11+
- `ts3` library (`pip install ts3`)

## Configuration
Update the following in `tsquicktravel.py`:
- `server_ip`: Your TeamSpeak server IP
- `username`: Your server query login username
- `password`: Your server query login password
- `quick_travel_map`: Map of source channel IDs to destination channel IDs

## How to Run
```bash
python tsquicktravel.py
