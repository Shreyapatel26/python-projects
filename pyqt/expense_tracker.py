import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class ExpenseTracker(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("expense tracker")
        self.setFixedSize(600, 600)
        self.total_expense = 0
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(20, 20, 20, 20)

        frame = QFrame()
        frame_layout = QVBoxLayout()
        frame_layout.setContentsMargins(20, 20, 20, 20)
        frame_layout.setSpacing(15)

        title = QLabel("Expense Tracker")
        title.setObjectName("title")

        top_layout = QHBoxLayout()
        top_layout.setSpacing(15)

        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        self.amount_input.setFixedHeight(45)
        self.amount_input.textChanged.connect(self.validate_amount)

        self.category_box = QComboBox()
        self.category_box.setFixedHeight(45)
        self.category_box.addItems([
            "Food",
            "Transport",
            "Shopping",
            "Entertainment",
            "Bills",
            "Other"
        ])

        self.error_label = QLabel("")
        self.error_label.setObjectName("error_label")

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Description")
        self.description_input.setFixedHeight(100)

        add_button = QPushButton("Add Expense")
        add_button.clicked.connect(self.add_expense)

        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_expense)

        left_layout.addWidget(self.amount_input)
        left_layout.addWidget(self.category_box)

        right_layout.addWidget(self.description_input)

        top_layout.addLayout(left_layout, 3)
        top_layout.addLayout(right_layout, 7)

        action_layout = QHBoxLayout()
        action_layout.addWidget(self.error_label)
        action_layout.addStretch()
        action_layout.addWidget(add_button)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Sr No.",
            "Amount",
            "Category",
            "Description"
        ])
        self.table.horizontalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter
)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.total_label = QLabel("Total Spent: ₹0.00")

        frame_layout.addWidget(title)
        frame_layout.addLayout(top_layout)
        frame_layout.addLayout(action_layout)
        frame_layout.addSpacing(20)
        frame_layout.addWidget(self.table, 1)
        frame_layout.addSpacing(10)
        frame_layout.addWidget(self.total_label)
        frame_layout.addSpacing(10)
        frame_layout.addWidget(delete_button)
        frame.setLayout(frame_layout)

        outer_layout.addWidget(frame)
        self.setLayout(outer_layout)
        self.frame = frame

    def validate_amount(self):
        text = self.amount_input.text().strip()

        if not text:
            self.error_label.setText("")
            return
        try:
            float(text)
            self.error_label.setText("")
        except ValueError:
            self.error_label.setText("Enter numbers only")  

    def add_expense(self):
        if self.error_label.text():
           return
        self.error_label.setText("")
        amount_text = (self.amount_input.text().strip())

        if not amount_text:
            self.error_label.setText("Enter an amount")
            return
        try:
            amount = float(amount_text)
        except ValueError:

            self.error_label.setText("Only numbers allowed")
            return

        category = (self.category_box.currentText())
        description = (
            self.description_input
            .toPlainText()
            .strip()
        )

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(
            row,
            0,
            QTableWidgetItem(str(row + 1))
        )
        self.table.setItem(
            row,
            1,
            QTableWidgetItem(f" ₹{amount:.2f}")
        )
        self.table.setItem(
            row,
            2,
           QTableWidgetItem(f" {category}")
        )
        self.table.setItem(
            row,
            3,
            QTableWidgetItem(f" {description}")
        )

        self.total_expense += amount
        self.total_label.setText(f"Total Spent: ₹{self.total_expense:.2f}")

        self.amount_input.clear()
        self.description_input.clear()

    def delete_expense(self):
        row = self.table.currentRow()

        if row < 0:
            return
        amount_text = (
            self.table
            .item(row, 1)
            .text()
        )
        amount = float(amount_text.replace("₹", ""))

        self.total_expense -= amount
        self.table.removeRow(row)
        self.total_label.setText(f"Total Spent: ₹{self.total_expense:.2f}")

    def apply_styles(self):
        self.setStyleSheet("""

            QWidget {
                background-color: #120d13;
                color: #f6eaf2;
                font-size: 14px;
            }

            QFrame {
                background-color: #22131d;
            }

            #title {
                font-size: 26px;
                font-weight: bold;
                padding-bottom: 10px;
            }

            QLineEdit,
            QTextEdit,
            QComboBox {
                background-color: #311b28;
                border: none;
                border-radius: 0px;
                padding: 10px;
                color: white;
            }

            QPushButton {
                background-color: #a93c7f;
                border: none;
                border-radius: 0px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #c04f93;
            }

            QTableWidget {
                background-color: #311b28;
                border: none;
                border-radius: 0px;
                gridline-color: #442435;
            }

            QHeaderView::section {
                background-color: #4b2840;
                border: none;
                border-radius: 0px;
                padding: 8px;
            }

            #error_label {
                color: red;
                font-weight: bold;
            }

        """)

app = QApplication(sys.argv)
window = ExpenseTracker()
window.show()
sys.exit(app.exec())
