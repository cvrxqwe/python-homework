import json

filename = "settings.json"

# 1. Create a dictionary with default settings
settings = {
    "theme": "light",
    "language": "English",
    "font_size": 14
}

# 2. Save to file (json.dump)
with open(filename, "w") as file:
    json.dump(settings, file, indent=4)
    print("Default settings saved to file.")

# 3. Read the file (simulating program restart) using json.load
with open(filename, "r") as file:
    loaded_settings = json.load(file)

# 4. Print the saved settings
print("\n--- Loaded Settings ---")
for key, value in loaded_settings.items():
    print(f"{key}: {value}")

# 5. Change one parameter and save again
loaded_settings["theme"] = "dark"
loaded_settings["font_size"] = 16
print("\nUser changed the theme and font size.")

# Save the updated dictionary back to the same file
with open(filename, "w") as file:
    json.dump(loaded_settings, file, indent=4)
    print("Updated settings saved to file.")