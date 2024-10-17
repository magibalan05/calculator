from flask import Flask, render_template, request

# Create a Flask instance
app = Flask(__name__)

# Route for the calculator page
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Route to perform the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve numbers and operation from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform the selected operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            result = 'Invalid operation'

        return render_template('calculator.html', result=result)

    except (ValueError, ZeroDivisionError):
        return render_template('calculator.html', result="Error! Invalid input.")

# Start the development server
if __name__ == '__main__':
    # Enable debug mode for auto-reloading and better error messages
    app.run(debug=True, host='0.0.0.0', port=5000)
