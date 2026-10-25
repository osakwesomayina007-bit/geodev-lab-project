import csv

def inspect_column( filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv. DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

lga_result = inspect_column("myarea.csv", "lgacode")
area_result = inspect_column("myarea.csv", "area_km2")

print("lga:", lga_result)
print("area:", area_result)

 
