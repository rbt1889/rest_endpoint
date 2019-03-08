from flask import Flask
from flask import jsonify

#Hardcoded list
numbers_to_add = list(range(10000001))

#Max size setting - could be omitted, but safer to have it
max_size = 10000001

# Static strings to be returned instead of a result, if a list length is bigger 
# than max_size or if it contains anything other than numbers
TOO_BIG = "Your list is too big"
NOT_NUMBERS = "Your list should contain only numbers"

def sum_of_list(some_list):
    """Method to calculate the sum of the numbers in the list"""
    if(len(some_list) < 10000002):
        try:
            total = sum(some_list)
        except TypeError:
            return NOT_NUMBERS
        else:
            return total
    else: 
        return TOO_BIG

# Create the application instance
app = Flask(__name__)

# Create a URL route for path "/"
@app.route('/')
def hello():
    hello_msg = 'Hello! Please go <a href="http://localhost:5000/total">here</a> to see the total'
    return hello_msg

# Create a URL route for path "/total"
@app.route("/total", methods=["GET"])
def show_sum():
    """Method to show the response in JSON format"""
    total = sum_of_list(numbers_to_add)
    return jsonify(
        total=total)

# Run the application if running in standalone mode
if __name__ == '__main__':
    app.run(debug=True)