### NOTE: I DID MY BEST HERE, DESPITE FAULTS FROM MY MACHINE AND EDITING ALONG THE WAY. PLEASE BE LENIENT. if you encounter issues. the problem might result either from the redis configuration that aligns to that of my won machine(i use a windows) or data loss due to compression.

# Hacker News Clone Project

This project is a Django-based web application that simulates some of the functionality of the Hacker News website. Users can view and interact with top-level items, view details of individual items (including comments), and perform actions on API-created items.

## Features

- Display top-level items and their children (comments).
- API for adding new items (not present in Hacker News).
- Updating and deleting items created through the API.
- User authentication and profiles.
- Voting, sorting, and pagination (creative additions).

## Setup

1. Clone the repository:
https://github.com/echewisi/hacker-news


2. Create a virtual environment and activate it:


3. Install project dependencies:
pip install -r requirements.txt


4. Set up the database:
py manage.py migrate


5. Start the development server:
py manage.py runserver


6. Access the application in your browser at http://localhost:8000.

## Usage

- View the list of top-level items at http://localhost:8000/items/
- View details of an item and its children at http://localhost:8000/item/<item_id>/
- Update an API-created item at http://localhost:8000/item/<item_id>/update/
- Delete an API-created item at http://localhost:8000/item/<item_id>/delete/
- Create a user profile and interact with creative features.

## Contributing

Feel free to contribute to this project by opening issues and pull requests. Suggestions and improvements are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
