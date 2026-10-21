from functools import wraps

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Logging decorator
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"-- Log: Executing method '{func.__name__}' --")
        return func(*args, **kwargs)
    return wrapper

# Role checking decorator
def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Check access using the private method
            if self._check_access(role):
                return func(self, *args, **kwargs)
            else:
                print(f"Access Denied: User '{self.user.name}' does not have the '{role}' role!")
        return wrapper
    return decorator

class AdminPanel:
    def __init__(self, user):
        self.user = user
        # Mock database of users
        self.users_db = ["Ivan", "Maria", "Peter"]

    # Private method (starts with an underscore)
    def _check_access(self, role):
        return self.user.role == role

    @log_action
    def view_users(self):
        print(f"User list: {self.users_db}")

    # Demo 1: First log the action, then check permissions
    @log_action
    @require_role("admin")
    def delete_user(self, username):
        if username in self.users_db:
            self.users_db.remove(username)
            print(f"User '{username}' has been successfully deleted.")
        else:
            print("User not found.")

    # Demo 2: First check permissions, then log the action if successful
    @require_role("admin")
    @log_action
    def change_settings(self, setting, value):
        print(f"Setting '{setting}' has been changed to '{value}'.")

# ==========================================
# Testing the System
# ==========================================

print("=== Tests for Admin ===")
admin = User("Max", "admin")
panel = AdminPanel(admin)

panel.view_users()
panel.delete_user("Ivan")
panel.change_settings("Theme", "Dark")

print("\n=== Tests for Regular User ===")
guest = User("Oleh", "guest")
panel2 = AdminPanel(guest)

# Works fine, no role required
panel2.view_users()

# Fails (not an admin), but logs the attempt because @log_action is on top
panel2.delete_user("Maria")

# Fails and does NOT log because @require_role blocks it before @log_action
panel2.change_settings("Theme", "Light")