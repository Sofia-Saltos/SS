# party_planner.py

import cgi

party_items = {
    0: ("Cake", 20),
    1: ("Balloons", 21),
    2: ("Music System", 10),
    3: ("Lights", 5),
    4: ("Catering Service", 8),
    5: ("DJ", 3),
    6: ("Photo Booth", 15),
    7: ("Tables", 7),
    8: ("Chairs", 12),
    9: ("Drinks", 6),
    10: ("Party Hats", 9),
    11: ("Streamers", 18),
    12: ("Invitation Cards", 4),
    13: ("Party Games", 2),
    14: ("Cleaning Service", 11)
}

def calculate_party_code(selected_indices):
    selected_items = []
    base_code = None
    
    for index in selected_indices:
        index = int(index)
        if index in party_items:
            selected_items.append(party_items[index][0])
            base_code = party_items[index][1] if base_code is None else base_code & party_items[index][1]

    return selected_items, base_code

def adjust_base_code(base_code):
    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"
    
    return base_code, message

def generate_html(selected_items, base_code, message):
    return f"""
    <html>
    <head>
        <title>Party Planner Results</title>
        <style>
            body {{ background-color: #ffccff; font-family: Arial, sans-serif; text-align: center; }}
            h2 {{ color: #d63384; }}
            p {{ color: #880e4f; font-size: 18px; }}
        </style>
    </head>
    <body>
        <h2>Selected Items:</h2>
        <p>{', '.join(selected_items)}</p>
        <h2>Base Party Code:</h2>
        <p>{base_code}</p>
        <h2>Final Message:</h2>
        <p>{message}</p>
    </body>
    </html>
    """

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
selected_indices = form.getlist("items")

selected_items, base_code = calculate_party_code(selected_indices)
base_code, message = adjust_base_code(base_code)

print(generate_html(selected_items, base_code, message))    