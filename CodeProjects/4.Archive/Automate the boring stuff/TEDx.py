import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

# Define the evaluation criteria and their respective weights
criteria = [
    {"name": "Idea", "weight": 30},
    {"name": "Vocabulary", "weight": 10},
    {"name": "Grammar", "weight": 10},
    {"name": "Fluency and Accuracy", "weight": 30},
    {"name": "Body Language", "weight": 10},
    {"name": "Creative", "weight": 10},
]

# Function to evaluate a single contestant
def evaluate_contestant():
    name = name_entry.text().strip()

    # Check if the name field is empty
    if not name:
        QMessageBox.warning(window, "Error", "Please enter the contestant's name.")
        return

    # Initialize the total score to 0
    total_score = 0

    # Create a string to store the evaluation details
    evaluation_details = f"Evaluation for {name}:\n"

    # Evaluate each criterion and add it to the total score
    for criterion in criteria:
        score = criterion_entries[criterion['name']].text()
        if not score.isdigit() or int(score) < 0 or int(score) > criterion["weight"]:
            QMessageBox.warning(window, "Error", f"Invalid {criterion['name']} score. Please enter a valid score.")
            return

        evaluation_details += f"{criterion['name']} ({criterion['weight']}%): {score}\n"
        total_score += int(score) * criterion["weight"] / 100

    # Provide overall feedback and assessment
    evaluation_details += f"\nTotal Score: {total_score:.2f}\n"
    evaluation_details += f"{name} has {'passed' if total_score >= 50 else 'failed'} the evaluation."

    QMessageBox.information(window, "Evaluation Result", evaluation_details)

# Create the application instance
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("TEDx Contestant Evaluation")

# Create and place the contestant name label and entry field
name_label = QLabel("Contestant's Name:")
name_entry = QLineEdit()

# Create and place the criteria labels and entry fields
criterion_entries = {}
for criterion in criteria:
    criterion_label = QLabel(f"{criterion['name']} ({criterion['weight']}%):")
    criterion_entry = QLineEdit()
    criterion_entries[criterion['name']] = criterion_entry

# Create and place the evaluate button
evaluate_button = QPushButton("Evaluate")
evaluate_button.clicked.connect(evaluate_contestant)

# Create the layout and add widgets
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_entry)

# Create a layout for criteria labels and entry fields
criteria_layout = QVBoxLayout()
for criterion in criteria:
    criterion_label = QLabel(f"{criterion['name']} ({criterion['weight']}%):")
    criterion_entry = QLineEdit()
    criterion_entries[criterion['name']] = criterion_entry
    criteria_layout.addWidget(criterion_label)
    criteria_layout.addWidget(criterion_entry)

layout.addLayout(criteria_layout)
layout.addWidget(evaluate_button)

# Set the layout on the window
window.setLayout(layout)

# Show the window
window.show()

# Execute the application's event loop
sys.exit(app.exec_())
