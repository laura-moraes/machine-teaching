def sort_csv(csv):
    items = csv.split(', ')
    items.sort()
    return ", ".join(items)
