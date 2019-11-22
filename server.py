from flask import Flask, request, render_template
import csv
app = Flask(__name__)
file_path = "./dht_data.csv"
my_port = 19237

#return HTML 
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
    return render_template('./index.html', values=values)

#receive sensor data 
@app.route('/dht', methods=['POST'])
def update_dht():
    try:
        time = request.form["time"]
        dht = request.form["dht"]
    except Exception as e:
        return "paramater is incorrect"
    #humidity = request.form["humidity"]
    #temperature = request.form["temperature"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + dht)
        return "Success to write!"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()
    return get_html()

#reading and retrieve sensor data
@app.route('/dht', methods=['GET'])
def get_dht():
    try:
        f = open(file_path, 'r')
        for row in f:
            dht = row
        return dht
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()

def write_csv():
    with open('./dht_data.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerows([get_dht()])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=my_port)
