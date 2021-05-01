from flask import Flask

# Set the flask application's name, list of available ports, and instantiate it
NAME='App'
PORTS = [5000,5001,5002,5003,5004,5005,5006,4999,4998,4997]
app = Flask(NAME)

# Global counter and a limit 
i=0
LIMIT = len(PORTS)

#**************************************************************************************************************
# WEIRD SNIPPET: define a try-except wrapper that uses concurrency to keep trying until the limit is reached***
#**************************************************************************************************************
def try_except_wrapper(f):
    global i
    try:
        f()
    except:
        if i==LIMIT: return
        i+=1
        try_except_wrapper(lambda: app.run(debug=True, host='localhost', port=str(PORTS[i])))

if __name__ == '__main__':
    try_except_wrapper(lambda: app.run(debug=True, host='0.0.0.0', port=str(PORTS[i])))
