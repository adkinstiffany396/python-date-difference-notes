from datetime import date

def solve(value):
    return (date.fromisoformat(value[1]) - date.fromisoformat(value[0])).days
