#(5)
items = {
    's1': 10, 's2': 8, 's3': 5,
    'p1': 10, 'p2': 8, 'p3': 5,
    't1': 10, 't2': 6,
    'b1': 10,
    'c1': 10,
    'sg1': 7,
    'pb1': 10,
    'sd1': 8, 'sd2': 5
}

def select_items(items, limit):
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    selected_items = []

    for item, _ in sorted_items:
        if len(selected_items) < limit:
            selected_items.append(item)
        else:
            break

    return selected_items

# Example usage
selected_items = select_items(items, 10)
print("Selected items:", selected_items)
