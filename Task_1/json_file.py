import json

def read_file() -> list:
    notes = []
    with open('Task_1\Write.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            notes.append(temp)
    return notes

def write_file(notes: list):
    with open('Task_1\Write.json', 'w', encoding='utf-8') as fout:
        for note in notes:
            fout.write(json.dumps(note) + '\n')