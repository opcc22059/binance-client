from json_loader import JsonLoader

keys = JsonLoader().getConst(
    ['.secret/'],
    key_ignore_pattern='.secret'
).get('.private_keys')