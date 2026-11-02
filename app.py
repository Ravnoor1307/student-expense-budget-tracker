from tkinter import *
from tkinter import messagebox

from dashboard import Dashboard


class ExpenseTrackerApp:

    def __init__(self):
        self.root = Tk()
        self.root.title("Expense Tracker")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')

        self.loginGui()

        self.root.mainloop()

    def loginGui(self):
        def submit_login():
            username = self.username_entry.get().strip()
            email = self.email_entry.get().strip()
            password = self.password_entry.get()

            if not username or not email or not password:
                messagebox.showerror(
                    "Missing information",
                    "Please enter your username, email, and password.",
                    parent=self.root,
                )
                return

            self.clear()
            try:
                self.dashboard = Dashboard(self.root, username)
            except ValueError as error:
                messagebox.showerror(
                    "Dashboard data error",
                    str(error),
                    parent=self.root,
                )
                self.loginGui()

        self.loginframe = Frame(self.root, bg='#f0f0f0')
        self.loginframe.pack(pady=50)

        self.login_label = Label(
            self.loginframe, text='Login', bg='#f0f0f0', font=('Arial', 16)
        )
        self.login_label.pack(pady=10)

        self.login_notice = Label(
            self.loginframe,
            text="Demo mode: credentials are not verified.",
            bg='#f0f0f0',
            fg='#666666',
        )
        self.login_notice.pack(pady=5)

        self.username_label = Label(self.loginframe, text='Username:', bg='#f0f0f0')
        self.username_label.pack(pady=5)

        self.username_entry = Entry(self.loginframe, bg='#ffffff')
        self.username_entry.pack(pady=5)

        self.email_label = Label(self.loginframe, text='Email:', bg='#f0f0f0')
        self.email_label.pack(pady=5)

        self.email_entry = Entry(self.loginframe, bg='#ffffff')
        self.email_entry.pack(pady=5)

        self.password_label = Label(self.loginframe, text='Password:', bg='#f0f0f0')
        self.password_label.pack(pady=5)

        self.password_entry = Entry(self.loginframe, bg='#ffffff', show='*')
        self.password_entry.pack(pady=5)

        self.login_button = Button(
            self.loginframe,
            text='Login',
            bg='#4CAF50',
            fg='#ffffff',
            command=submit_login,
        )
        self.login_button.pack(pady=30)

        self.clear_button = Button(
            self.loginframe,
            text='Clear',
            command=self.clear,
        )
        self.clear_button.pack(pady=5)

        self.signup_button = Button(
            self.loginframe,
            text='Sign Up',
            command=self.signup,
        )
        self.signup_button.pack(pady=5)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def signup(self):
        self.clear()

        def return_to_login():
            self.clear()
            self.loginGui()

        def submit_signup():
            username = self.signup_username_entry.get().strip()
            email = self.signup_email_entry.get().strip()
            password = self.signup_password_entry.get()

            if not username or not email or not password:
                messagebox.showerror(
                    "Missing information",
                    "Please enter your username, email, and password.",
                    parent=self.root,
                )
                return

            messagebox.showwarning(
                "Sign up unavailable",
                "Account creation is not configured yet, so your information has not been saved.",
                parent=self.root,
            )

        self.signupframe = Frame(self.root, bg='#f0f0f0')
        self.signupframe.pack(pady=50)

        self.signup_label = Label(
            self.signupframe,
            text='Sign Up',
            bg='#f0f0f0',
            font=('Arial', 16),
        )
        self.signup_label.pack(pady=10)

        self.signup_username_label = Label(
            self.signupframe, text='Username:', bg='#f0f0f0'
        )
        self.signup_username_label.pack(pady=5)
        self.signup_username_entry = Entry(self.signupframe, bg='#ffffff')
        self.signup_username_entry.pack(pady=5)

        self.signup_email_label = Label(
            self.signupframe, text='Email:', bg='#f0f0f0'
        )
        self.signup_email_label.pack(pady=5)
        self.signup_email_entry = Entry(self.signupframe, bg='#ffffff')
        self.signup_email_entry.pack(pady=5)

        self.signup_password_label = Label(
            self.signupframe, text='Password:', bg='#f0f0f0'
        )
        self.signup_password_label.pack(pady=5)
        self.signup_password_entry = Entry(
            self.signupframe, bg='#ffffff', show='*'
        )
        self.signup_password_entry.pack(pady=5)

        self.create_account_button = Button(
            self.signupframe,
            text='Create Account',
            bg='#4CAF50',
            fg='#ffffff',
            command=submit_signup,
        )
        self.create_account_button.pack(pady=20)

        self.signup_clear_button = Button(
            self.signupframe,
            text='Clear',
            command=self.clear,
        )
        self.signup_clear_button.pack(pady=5)

        self.back_to_login_button = Button(
            self.signupframe,
            text='Back to Login',
            command=return_to_login,
        )
        self.back_to_login_button.pack(pady=5)

expense_tracker_app = ExpenseTrackerApp()