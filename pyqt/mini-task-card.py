import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QDate

app = QApplication(sys.argv)

# WINDOW AND MAIN WIDGET
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setFixedSize(320, 500)
window.setWindowTitle("Mini Task Card")

# LAYOUTS
base_layout = QVBoxLayout()
base_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
base_layout.setContentsMargins(17, 17, 17, 17)

input_layout = QHBoxLayout()
frame_container_layout = QVBoxLayout()
frame_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

# WIDGETS
title = QLabel("🚀🌿 Get Things Done!")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
title.setObjectName("title")

input = QLineEdit()
input.setObjectName("input")
input.setPlaceholderText("Add task")
input.setFixedHeight(40)

add_button = QPushButton("+")
add_button.setFixedHeight(40)
add_button.setFixedWidth(40)

scroll = QScrollArea()
scroll.setWidgetResizable(True)
scroll.setFrameShape(QFrame.Shape.NoFrame)

container = QWidget()
container.setObjectName("container")

# FUNCTION
def add_task():
    text = input.text()

    if not text:
        return

    # frame
    frame = QFrame()
    frame.setObjectName("cards")
    frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)

    frame_layout = QVBoxLayout()
    frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    frame_layout.setContentsMargins(15, 15, 15, 15)
    frame_layout.setSpacing(10)

    # checkbox, description and date label
    checkbox = QCheckBox(text)
    checkbox.stateChanged.connect(
    lambda state, cb=checkbox: task_checked(state, cb)
)
    
    description = QLineEdit()
    description.setObjectName("des")
    description.setPlaceholderText("Add a description...")

    date = QLabel()
    date.setAlignment(Qt.AlignmentFlag.AlignRight)
    date.setText(QDate.currentDate().toString("dd-MM-yyyy dddd"))
    date.setObjectName("date")

    # adding widgets into frame
    frame_layout.addWidget(checkbox)
    frame_layout.addWidget(description)
    frame_layout.addWidget(date)

    frame.setLayout(frame_layout)

    # frame to main container
    frame_container_layout.addWidget(frame)

    input.clear()

add_button.clicked.connect(add_task)

def task_checked(state, checkbox):
    font = checkbox.font()
    font.setStrikeOut(state == Qt.CheckState.Checked.value)
    checkbox.setFont(font)

    if state == Qt.CheckState.Checked.value:
        checkbox.setStyleSheet("color: #A97772;")
    else:
        checkbox.setStyleSheet("")

# ASSIGNING LAYOUTS
base_layout.addWidget(title)

input_layout.addWidget(input)
input_layout.addWidget(add_button)
base_layout.addLayout(input_layout)

frame_container_layout = QVBoxLayout(container)
frame_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
scroll.setWidget(container)
base_layout.addWidget(scroll)

central_widget.setLayout(base_layout)

# STYLESHEET
BG = "#eaaba6"
CARDS_BG = "#dba19d"
FONT = "#592B26"
INPUT_BG = "#c7847f"
HOVER_BG = "#d4938f"

window.setStyleSheet(f"""
QMainWindow {{
    background: {BG};
}}

#title {{
    font: bold 19px;
    padding-bottom: 20px;
    padding-top: 10px;
    color: {FONT};
}}

#input {{
    border: none;
    padding: 10px;
    background: {INPUT_BG};
    color: {FONT};
    font-size: 14px;
    border-radius: 2px;
}}

#input:hover {{
    background: {HOVER_BG};
}}

QPushButton {{
    border: none;
    padding: 0px;
    background: {INPUT_BG};
    font-size: 20px;
    color: {FONT};
    border-radius: 2px;
}}

QPushButton:hover {{
    background: {HOVER_BG};
}}

#container {{
    background: {BG};
}}

#cards {{
    background: {CARDS_BG};
    border-radius: 2px;
    margin-top: 10px;
}}

QCheckBox {{
    font: bold 14px;
    color: {FONT};
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border: 2px solid {INPUT_BG};
}}

QCheckBox::indicator:checked {{
    background-color: {INPUT_BG};
    border: 2px solid {INPUT_BG};
}}

#des {{
    padding: 4px;
    background: {CARDS_BG};
    border: none;
    color: {FONT};
    font: italic 12.4px;
}}

#date {{
    font-size: 11px;
    color: {FONT};
}}

QScrollArea {{
    border: none;
    background: transparent;
}}
QScrollBar:vertical {{
    width: 0px;
    background: transparent;
}}

QScrollBar::handle:vertical {{
    background: transparent;
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {{
    background: transparent;
}}

QScrollBar:horizontal {{
    height: 0px;
    background: transparent;
}}
""")

window.show()
app.exec()
