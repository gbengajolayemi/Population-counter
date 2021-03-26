import pymongo
import webbrowser

client = pymongo.MongoClient("")
db = client["OpenD"]
col = db["States"]
data = [{'state': 'Abia', 'value': 10.2},
        {'state': 'Adamawa', 'value': 10.1,},
        {'state': 'Akwa Ibom', 'value': 10.3,},
        {'state': 'Anambra', 'value': 14.6,},
        {'state': 'Bauchi', 'value': 1.7,},
        {'state': 'Bayelsa', 'value': 6.1,},
        {'state': 'Benue', 'value': 1.9,},
        {'state': 'Borno', 'value': 7.9,.38},
        {'state': 'Cross River', 'value': 19.2, },
        {'state': 'Delta', 'value': 14.2,},
        {'state': 'Ebonyi', 'value': 0.2,},
        {'state': 'Edo', 'value': 1.7,},
        {'state': 'Ekiti', 'value': 6.1,},
        {'state': 'Enugu', 'value': 6.1,},
        {'state': 'Gombe', 'value': 2.7,},
        {'state': 'Imo', 'value': 8.3,},
        {'state': 'Jigawa', 'value': 22.3,},
        {'state': 'Kaduna', 'value': 14.9,},
        {'state': 'Kano', 'value': 21.4,},
        {'state': 'Katsina', 'value': 5.3,},
        {'state': 'Kebbi', 'value': 7.7,},
        {'state': 'Kogi', 'value': 6.5,},
        {'state': 'Kwara', 'value': 4.8,.},
        {'state': 'Lagos', 'value': 15.4,},
        {'state': 'Nasarawa', 'value': 4,},
        {'state': 'Niger', 'value': 11.3,},
        {'state': 'Ogun', 'value': 4.8, },
        {'state': 'Ondo', 'value': 4.7,},
        {'state': 'Osun', 'value': 3,},
        {'state': 'Oyo', 'value': 3.5,},
        {'state': 'Plateau', 'value': 5.2,},
        {'state': 'Rivers', 'value': 3,},
        {'state': 'Sokoto', 'value': 6.3,},
        {'state': 'Taraba', 'value': 4.4,},
        {'state': 'Yobe', 'value': 11,.43},
        {'state': 'Zamfara', 'value': 6.1,},
        {'state': 'FCT', 'value': 12.9,},
]
x = col.insert_many(data)


tbl = "<tr><td>State</td><td>Percentage</td></tr>"
data.append(tbl)

for y in col.find():
    a = "<tr><td>%s</td>" % y['state']
    data.append(a)
    b = "<td>%s</td></tr>" % y['value']
    data.append(b)

contents = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CEN 414 Project</title>
</head>
<body>
<h2>Below is a table showing Feburary 2020 disembursement for states of the federation
</h2>
<form action = "map.html" method = "post">
<label for= "states">Choose a state:</label>

<select name="states" id="states">
  <option value="Abia">Abia</option>
  <option value="Adamawa">Adamawa</option>
  <option value="Anambra">Anambra</option>
  <option value="Bauchi">Bauchi</option>
  <option value="Bayelsa">Bayelsa</option>
  <option value="Bauchi">Bauchi</option>
  <option value="Bayelsa">Bayelsa</option>
  <option value="Benue">Benue</option>
  <option value="Borno">Borno</option>
  <option value="Cross River">Cross River</option>
  <option value="Delta">Delta</option>
  <option value="Ebonyi">Ebonyi</option>
  <option value="Edo">Edo</option>
  <option value="Ekiti">Ekiti</option>
  <option value="Enugu">Enugu</option>
  <option value="Gombe">Gombe</option>
  <option value="Imo">Imo</option>
  <option value="Jigawa">Jigawa</option>
  <option value="Kaduna">Kaduna</option>
  <option value="Kano">Kano</option>
  <option value="Katsina">Katsina</option>
  <option value="Kebbi">Kebbi</option>
  <option value="Kogi">Kogi</option>
  <option value="Kwara">Kwara</option>
  <option value="Kwara">Kwara</option>
  <option value="Lagos">Lagos</option>
  <option value="Nasarawa">Nasarawa</option>
  <option value="Niger">Niger</option>
  <option value="Ogun">Ogun</option>
  <option value="Ondo">Ondo</option>
  <option value="Osun">Osun</option>
  <option value="Oyo">Oyo</option>
  <option value="Plateau">Plateau</option>
  <option value="Rivers">Rivers</option>
  <option value="Sokoto">Sokoto</option>
  <option value="Taraba">Taraba</option>
  <option value="Yobe">Yobe</option>
  <option value="Zamfara">Zamfara</option>
  <option value="FCT">FCT</option>
</select>
<br></br>
<input type = "submit" value = "Submit">
</form>

<table>
    %s
</table>
</body>
</html>
''' % data

filename = 'Surf.html'


def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)
