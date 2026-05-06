import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from database import run_query
from queries import QUERIES


class OneCityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OneCity Seattle Database Query App")
        self.root.geometry("1100x650")

        self.current_columns = []
        self.current_rows = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="OneCity Seattle Database Query App",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="Select a city insight query and view the results.",
            font=("Arial", 11)
        )
        subtitle.pack(pady=5)

        query_frame = tk.Frame(self.root)
        query_frame.pack(pady=10)

        tk.Label(
            query_frame,
            text="Choose Query:",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=5)

        self.query_var = tk.StringVar()

        self.query_dropdown = ttk.Combobox(
            query_frame,
            textvariable=self.query_var,
            values=list(QUERIES.keys()),
            width=65,
            state="readonly"
        )
        self.query_dropdown.pack(side=tk.LEFT, padx=5)

        run_button = tk.Button(
            query_frame,
            text="Run Query",
            command=self.execute_selected_query,
            width=15
        )
        run_button.pack(side=tk.LEFT, padx=5)

        export_button = tk.Button(
            query_frame,
            text="Export CSV",
            command=self.export_csv,
            width=15
        )
        export_button.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            fg="blue"
        )
        self.status_label.pack(pady=5)

        table_frame = tk.Frame(self.root)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame)

        y_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        x_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

    def execute_selected_query(self):
        query_name = self.query_var.get()

        if not query_name:
            messagebox.showwarning(
                "No Query Selected",
                "Please select a query first."
            )
            return

        query = QUERIES.get(query_name)

        try:
            self.status_label.config(text="Running query...", fg="orange")
            self.root.update_idletasks()

            columns, rows = run_query(query)

            self.current_columns = columns
            self.current_rows = rows

            self.update_table(columns, rows)

            self.status_label.config(
                text=f"Query completed. Rows returned: {len(rows)}",
                fg="green"
            )

        except Exception as error:
            self.status_label.config(text="Query failed.", fg="red")
            messagebox.showerror("Error", str(error))

    def update_table(self, columns, rows):
        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = columns
        self.tree["show"] = "headings"

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=160, anchor="center")

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def export_csv(self):
        if not self.current_columns or not self.current_rows:
            messagebox.showwarning(
                "No Data",
                "Run a query before exporting results."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save query results as CSV"
        )

        if not file_path:
            return

        try:
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(self.current_columns)
                writer.writerows(self.current_rows)

            messagebox.showinfo(
                "Export Successful",
                f"Results exported to:\n{file_path}"
            )

        except Exception as error:
            messagebox.showerror("Export Error", str(error))


def main():
    root = tk.Tk()
    app = OneCityApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()