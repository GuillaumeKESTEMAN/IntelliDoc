# IntelliDoc

## Installation

- create `.env` file from `.env.sample` and define a password
- launch `docker compose up --build`
- wait approximately 10 min during build process

## Usage

- go to scripts container console
- execute `python main.py`

## Functionalities

### 1. Import custom document

You can import to the database a custom document (title, text and source) in the database.

### 2. Import french wikipedia dataset

You can download the wikipedia dataset and import X items into the database (you can choose the number of items you wish to import).

This can be a long process, as there is a lot of data in the wikipedia dataset, and we also need to reformat the data.

### 3. Import from import_data.json

You can import to the database data from json file which is connected to the container (so you can update it when the container is running).

Example:
```json
[
	{
		"title": "your title",
		"text": "your text",
		"link": "your link",
	}
]
```

### 4. Reset database index

You can reset all data in the database to restart with new data without rebuilding the containers.

### 5. Make a textual document research

You can make a textual document research (without AI).

### 6. Make a semantic document research

You can make a semantic document research (with AI).