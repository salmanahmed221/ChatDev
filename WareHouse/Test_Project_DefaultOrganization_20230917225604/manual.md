# Flask App for Student Information

This Flask app allows you to collect and store student information in a SQLite database. The app includes a web page where you can enter the student's name, age, education, address, city, and phone number. After submitting the form, the student's record will be saved in the database.

## Installation

To run this Flask app, you need to install the required dependencies listed in the `requirements.txt` file. You can do this by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the Flask app files are located.

2. Run the following command to start the Flask development server:

   ```
   python main.py
   ```

3. Open a web browser and go to `http://localhost:5000` to access the student information form.

4. Fill in the student's information in the form fields and click the "Submit" button.

5. After submitting the form, you will be redirected to a success page indicating that the record has been saved successfully.

## Files

- `main.py`: This is the main file for the Flask app. It contains the routes and logic for handling form submissions and saving records to the database.

- `models.py`: This file defines the database model for the student record. It uses SQLAlchemy to define the table structure and columns.

- `forms.py`: This file defines the form for collecting student information. It uses Flask-WTF to handle form validation and rendering.

- `index.html`: This HTML template file defines the structure and layout of the student information form.

- `success.html`: This HTML template file is displayed after a successful form submission.

- `database.py`: This file initializes the SQLite database using SQLAlchemy.

- `requirements.txt`: This file lists the required dependencies for running the Flask app.

## Customization

You can customize the app by modifying the HTML templates (`index.html` and `success.html`) to change the layout or add additional fields. You can also modify the database model (`models.py`) to add or remove columns as needed.

## Conclusion

This Flask app provides a simple and easy way to collect and store student information in a SQLite database. By following the installation and usage instructions, you can quickly set up and run the app on your local machine. Feel free to customize the app to fit your specific requirements.