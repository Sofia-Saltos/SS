<!DOCTYPE html>
<html>
<head>
    <title>Party Planner</title>
    <style>
        body { background-color: #ffe6f2; font-family: Arial, sans-serif; text-align: center; }
        h2 { color: #d63384; }
        form { background-color: #ff99cc; padding: 20px; display: inline-block; border-radius: 10px; }
        input[type="submit"] { background-color: #d63384; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; }
        input[type="checkbox"] { margin: 5px; }
    </style>
</head>
<body>
    <h2>Plan Your Party!</h2>
    <form action="party_planner.py" method="get">
        <h3>Select party items:</h3>

        <?php
        $party_items = [
            0 => "Cake", 1 => "Balloons", 2 => "Music System", 3 => "Lights",
            4 => "Catering Service", 5 => "DJ", 6 => "Photo Booth", 7 => "Tables",
            8 => "Chairs", 9 => "Drinks", 10 => "Party Hats", 11 => "Streamers",
            12 => "Invitation Cards", 13 => "Party Games", 14 => "Cleaning Service"
        ];

        foreach ($party_items as $index => $name) {
            echo "<label><input type='checkbox' name='items[]' value='$index'> $name</label><br>";
        }
        ?>

        <br>
        <input type="submit" value="Generate Party Plan">
    </form>
</body>
</html>