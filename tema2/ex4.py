def compose(notes, moves, start):
    song = []
    position = start
    song.append(notes[position])

    for move in moves:
        position = (position + move) % len(notes)
        song.append(notes[position])

    return song


result = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print(result)