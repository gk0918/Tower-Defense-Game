import json

def save_game(stats, towers):
    data = {
        "money": stats.money,
        "lives": stats.lives,
        "wave": stats.wave,
        "towers": [
            {
                "x": t.pos[0],
                "y": t.pos[1],
                "type": t.type,
                "level": t.level
            } for t in towers
        ]
    }
    with open("savegame.json", "w") as f:
        json.dump(data, f)

def load_game(stats, towers, Tower):
    try:
        with open("savegame.json") as f:
            data = json.load(f)
        stats.money = data["money"]
        stats.lives = data["lives"]
        stats.wave = data["wave"]
        towers.clear()
        for t in data["towers"]:
            tower = Tower((t["x"], t["y"]), t["type"])
            for _ in range(t["level"] - 1):
                tower.upgrade()
            towers.append(tower)
        return True
    except:
        return False

