# app.py

from flask import Flask, render_template

app = Flask(__name__)

# # Define a function that generates a message
# def homepage_message():
#     return "Welcome to the Home Page with Flask!"

# Define the homepage route
@app.route('/')
def home():
    message = "hello World"  # Call the function
    return render_template('index.html', message=message)  # Pass the message to HTML

# Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
     app.run(debug=True)