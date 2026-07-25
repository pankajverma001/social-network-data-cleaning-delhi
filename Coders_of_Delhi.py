import json


def load_data(filename):
    """Load JSON data from file."""
    with open(filename, "r") as file:
        return json.load(file)


def clean_data(data):
    """Clean the social network dataset."""

    # Remove users with empty names
    data["users"] = [
        user for user in data["users"]
        if user["name"].strip()
    ]

    # Remove duplicate friend IDs
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Remove users with no friends and no liked pages
    data["users"] = [
        user for user in data["users"]
        if user["friends"] or user["liked_pages"]
    ]

    # Remove duplicate pages by page ID
    unique_pages = {}

    for page in data["pages"]:
        unique_pages[page["id"]] = page

    data["pages"] = list(unique_pages.values())

    return data


def save_data(data, filename):
    """Save cleaned data to JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def display_users(data):
    """Display user and page information."""

    print("\nUsers and their connections\n")

    for user in data["users"]:
        print(
            f"{user['id']} - {user['name']} is friends with: "
            f"{user['friends']} and liked pages are {user['liked_pages']}"
        )

    print("\nPages Information\n")

    for page in data["pages"]:
        print(f"{page['id']} {page['name']}")


def main():
    input_file = "data3.json"
    output_file = "Cleaned_data3.json"

    data = load_data(input_file)
    cleaned_data = clean_data(data)

    save_data(cleaned_data, output_file)

    print("Data has been cleaned successfully!")

    display_users(cleaned_data)


if __name__ == "__main__":
    main()
