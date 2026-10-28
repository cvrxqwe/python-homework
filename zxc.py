#Task 3

# Settings History Stack Class
class SettingsHistory:
    def __init__(self):
        # A simple Python list acts as our stack
        self.stack = []

    # 1. Save a description of each change (Push operation)
    def save_change(self, change_description):
        # .append() adds an item to the top of the stack (end of the list)
        self.stack.append(change_description)
        print(f"Saved: '{change_description}'")

    # 2. Output the latest change without removing it (Peek operation)
    def show_latest(self):
        if not self.stack:
            print("History is empty. No recent changes.")
        else:
            # [-1] gets the last element of the list
            print(f"Latest change: '{self.stack[-1]}'")

    # 3. Remove the latest change from the stack (Pop / Undo operation)
    def undo_last_change(self):
        if not self.stack:
            print("Nothing to undo. History is empty.")
        else:
            # .pop() removes and returns the last element from the list
            removed_change = self.stack.pop()
            print(f"Undo action: Removed '{removed_change}'")

    # 4. Show the history (from newest to oldest)
    def show_history(self):
        print("\n--- Settings History (Newest to Oldest) ---")
        if not self.stack:
            print("  [Empty]")
        else:
            # reversed() allows us to read the stack from top to bottom
            for index, change in enumerate(reversed(self.stack), start=1):
                print(f"  {index}. {change}")
        print("-------------------------------------------\n")


# Testing the System

settings = SettingsHistory()

# 1. User changes settings (Pushing to stack)
print("=== Adding Changes ===")
settings.save_change("Language changed to Ukrainian")
settings.save_change("Theme changed to Dark Mode")
settings.save_change("Font size increased to 16px")
settings.save_change("Volume set to 80%")

# 2. Show the latest change
print("\n=== Checking Latest Change ===")
settings.show_latest()

# 3. Undo the latest change (User decided they want the old volume back)
print("\n=== Undoing Last Action ===")
settings.undo_last_change()

# 4. Show history after undo
print("\n=== History After Undo ===")
settings.show_history()