def task3():
    community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
    result = []
    for member in community_members:
        if "a" in member:
            result.append(member)
    return len(result)

if __name__ == "__main__":
    print(f"length: {task3()}")

