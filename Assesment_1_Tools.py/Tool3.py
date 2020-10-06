NFL = {
    "player1" : {
        "name" : "Patrick Mahomes",
        "position" : "Quarterback",
        "team" : "Kansas City",
        "number" : 15,
    },
    "player2" : {
        "name" : "Ezekiel Elliot",
        "position" : "Running Back",
        "team" : "Dallas",
        "number" : 21,
    },
    "player3" : {
        "name" : "Deandre Hopkins",
        "position" : "Wide Receiver",
        "team" : "Arizona",
        "number" : 10,
    }
}

NFL["player3"]["sport"] = "Football"

print(len(NFL))
print(NFL.get("player3"))