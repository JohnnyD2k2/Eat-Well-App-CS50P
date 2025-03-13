# Eat Well App
#### Video Demo: [https://youtu.be/2DAh1cZ9N14?si=7t4s8f3UvLAxB_qS]

## Definition
The **Eat Well App** is an interactive web application built using Gradio, designed to assist users in planning and tracking healthy, balanced meals. This app provides a user-friendly interface for selecting nutritious recipes, calculating nutritional values (calories, protein, etc.), and managing meal plans for a week. It’s ideal for health-conscious individuals, dietitians, or anyone looking to maintain a balanced diet. The project is structured with the following files:
- `healthy_menu.csv`: A CSV file containing the menu data, including dish names, categories, calories, protein, prices (in Vietnamese Dong, VND), and allergy information.
- `project.py`: The main Python script implementing the app’s logic and Gradio interface.
- `test_project.py`: This script is for testing functions of the main Python script.
- `README.md`: This documentation file, providing an overview and instructions.

## Libraries

**GRADIO**: Gradio is a Python library that allows developers to create customizable, shareable web interfaces for machine learning models, data apps, or any Python function. In this project, it’s used to build an interactive, browser-based interface for users to browse the menu, view dish details, and manage their cart. [(Read more)](https://www.gradio.app/)

PANDAS: Pandas is a powerful data analysis and manipulation library for Python, used here to read and process the `healthy_menu.csv file`, enabling dynamic data handling for the menu and dish information. [(Read more)](https://pandas.pydata.org/)

## Installing Libraries
There is a `requirements.txt` file that lists all the libraries required for this project. You can install them easily using the following pip command:

```bash
pip install -r requirements.txt
```

## Usage
To run the Eat Well App, execute the following command in your terminal:

```bash
python project.py
```

Upon launching, the app opens a shareable web interface in your default browser, displaying a clean, dark-themed layout with the following structure:

<img width="959" alt="cs50" src="https://github.com/user-attachments/assets/6390e5f1-3f74-4ea9-8822-aee944679a90" />


Users can select dishes from radio buttons under each category, view detailed information (calories, protein, price, allergens) by selecting a dish, add items to their cart using the "ADD TO CART" button, and clear the cart with the "CLEAR CART" button. The app updates dynamically, showing totals for price, calories, and protein in the cart. Users can exit by closing the browser or terminating the script (`CTRL + C` in the terminal).

## Functioning
The `project.py` file contains 8 functions, including the main function, to implement the Eat Well App. Below is a detailed breakdown of its functionality:

`main()` Function:
This function launches the Gradio interface by calling `display()`, initializing the app’s web-based UI.

`get_appetizers()`, `get_main()`, `get_desserts()` Functions:
These functions retrieve lists of dish names from the `healthy_menu.csv` file for their respective categories (Appetizers, Main Course, Desserts) using Pandas, returning them for display in the Gradio radio buttons.

`get_info(dish_name)` Function:
Takes a dish name as an argument, queries the CSV data using Pandas, and returns formatted Markdown text with the dish’s details, including calories, protein, price, and allergy information. If the dish isn’t found, it returns an error message.

`add_to_cart(dish_name)` Function:
Takes a dish name, adds it to a global cart list with its price, calories, and protein, and returns an updated cart summary in Markdown format, showing individual items, total price, total calories, and total protein.

`clear_cart()` Function:
Clears the global cart list and returns a message indicating an empty cart.

`display()` Function:
Creates the Gradio interface with columns for menu selection, dish details, and cart management. It uses radio buttons for dish selection, buttons for adding to cart and clearing, and Markdown components for displaying details and cart status, linking functions to update dynamically based on user interactions.

Author: [Dang Tuan Minh].
