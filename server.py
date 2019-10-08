from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./humidity_data.csv"
my_port = 19237

@app.route('/', methods=['GET'])
def get_html():
    try:
        f = open(file_path, 'r')
        for row in f:
            dht = row
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()
    values = dht.split(',')
    return render_template('./index.html', time = values[0], humidity = values[1], temperature = values[2])

@app.route('/dht', methods=['POST'])
def update_dht():
    time = request.form["time"]
    humidity = request.form["humidity"]
    temperature = request.form["temperature"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + humidity + "," + temperature)
        return "Success to write!"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/dht', methods=['GET'])
def get_dht():
    try:
        f = open(file_path, 'r')
        for row in f:
            dht = row
        return dht.split(',')
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=my_port)
