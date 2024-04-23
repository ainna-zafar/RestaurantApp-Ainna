# RestaurantApp-Ainna

Below is a README file based on your instructions:

---

# Restaurant Data Retrieval Application

## Description
This application fetches restaurant data based on a selected postcode using the Just Eat API. It gives information about the restaurant names, cuisines, ratings, and addresses in a web interface.

## How to Build, Compile, and Run the Solution
To run the application, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
   ```
   cd restaurant-data-retrieval
   pip install -r requirements.txt
   ```

3. **Run the Application**: Execute the `app.py` file to start the Flask server:
   ```
   python app.py
   ```
   The application will start running on `http://127.0.0.1:5000/`. Open this URL in your web browser to view the restaurant data.

## Assumptions and Clarifications
- The application assumes that the provided postcode is valid and corresponds to a location with available restaurant data.
- It's assumed that the Just Eat API returns restaurant data in the expected format and structure.
- The application limits the displayed data to the first 10 restaurants returned by the API.

## Improvements
Some improvements that could be made to the solution include:
- Adding error handling to gracefully handle cases where the API request fails or returns unexpected data.
- Implementing pagination to retrieve and display more than 10 restaurants if available.
- Enhancing the user interface with additional features such as search functionality or filtering options.

---

