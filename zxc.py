#Task 5

# 1. Node Class (Tab)
class Tab:
    def __init__(self, title, url):
        self.title, self.url = title, url
        self.prev = self.next = None  # Multiple assignment on one line


# 2. TabManager Class
class TabManager:
    def __init__(self):
        self.head = self.tail = self.active = None

    def open_tab(self, title, url):
        new_tab = Tab(title, url)
        if not self.head:
            self.head = self.tail = self.active = new_tab
        else:
            # Re-link pointers compactly
            self.tail.next, new_tab.prev = new_tab, self.tail
            self.tail = new_tab
        print(f"Opened: '{title}'")

    # Combined next/prev tab into one method
    def switch(self, forward=True):
        target = self.active.next if forward else self.active.prev
        if target:
            self.active = target
            print(f"Switched to: '{self.active.title}'")
        else:
            print("Cannot move further.")

    def close_tab(self, title):
        curr = self.head
        # Quick search
        while curr and curr.title != title:
            curr = curr.next

        if not curr:
            return print(f"Tab '{title}' not found.")

        # Fallback for active tab (if prev is None, it takes next)
        if curr == self.active:
            self.active = curr.prev or curr.next

        # Re-link pointers (bypass the closed tab)
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        print(f"Closed: '{title}'")

    # Combined forward/backward display into one method
    def show(self, reverse=False):
        print(f"\n--- Tabs ({'Right to Left' if reverse else 'Left to Right'}) ---")
        curr = self.tail if reverse else self.head

        while curr:
            mark = "[*]" if curr == self.active else "[ ]"
            print(f"  {mark} {curr.title}")
            # Move to the next or previous depending on the mode
            curr = curr.prev if reverse else curr.next


# Testing the System
browser = TabManager()

browser.open_tab("Google", "google.com")
browser.open_tab("YouTube", "youtube.com")
browser.open_tab("GitHub", "github.com")

browser.switch(forward=True)  # Go to YouTube
browser.switch(forward=False)  # Go back to Google

browser.close_tab("Google")  # Close active tab
browser.show()  # Default: forward
browser.show(reverse=True)  # Backward