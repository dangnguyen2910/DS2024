data = [
   "which witch bitch did my bitch witch snitch on like the bitch witch she is not unlike the swiss witch bitch who snitched on the bitch witch that was swiss"
]

def mapping(data_chunk):
    key_value_pairs = []
    for line in data_chunk:
        words = line.split()
        for word in words:
            key_value_pairs.append((word.lower(), 1))
    return key_value_pairs

def sort_shuffle(mapped_data):
    grouped_data = {}
    for key, value in mapped_data:
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(value)
    return grouped_data

def reducing(grouped_data):
    reduced_data = {}
    for key, values in grouped_data.items():
        reduced_data[key] = sum(values)
    return reduced_data

mapped_data = []
for chunk in data:
    mapped_data.extend(mapping([chunk]))  

print("Mapped Data:", mapped_data)

shuffled_data = sort_shuffle(mapped_data)
print("Shuffled Data:", shuffled_data)

reduced_data = reducing(shuffled_data)
print("Reduced Data (Word Count):", reduced_data)
