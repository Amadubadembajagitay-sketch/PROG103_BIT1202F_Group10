 PROG103_BIT1202F_Group10# KrioHealth Clinic Queue Management System

 Project Overview
The KrioHealth Clinic Queue Management System is a simple desktop application developed using Python and the Tkinter GUI library. The system helps clinics manage patient queues by allowing staff to register patients, display the waiting list, serve patients in order of arrival (First-In, First-Out), and clear the queue when needed.

This project supports Sustainable Development Goal (SDG) 3: Good Health and Well-being by improving patient organization and reducing waiting time in healthcare facilities.

---
 Features

- Register new patients
- Store Patient ID, Name, Age, and Medical Condition
- Display the current waiting queue
- Serve patients using FIFO (First In, First Out)
- Clear the entire queue
- Validate user input
- User-friendly graphical interface

---

 Technologies Used

- Python 3
- Tkinter (GUI)
- Object-Oriented Programming (OOP)

---

 Classes

Patient
Represents a patient with the following information:
- Patient ID
- Full Name
- Age
- Medical Condition

Methods:
- get_info() - Returns the patient's information as a formatted string.

---

 KrioHealthQueue
Manages the patient queue.

Methods:
- add_patient()
- serve_next()
- get_queue_display()

---

Functions

add_to_queue()
- Reads user input
- Validates the data
- Creates a Patient object
- Adds the patient to the queue
- Updates the queue display

 update_queue_display()
Refreshes the queue shown on the screen.

 serve_next_patient()
Removes the first patient from the queue and displays their information.

 clear_fields()
Clears all input boxes after a patient is successfully added.

---

 Queue Algorithm

The system uses the FIFO (First In, First Out) queue algorithm.

Example:

Patient A enters

Patient B enters

Patient C enters

Serving order:
1. Patient A
2. Patient B
3. Patient C

---

 Input Validation

The program checks that:
- All fields are completed.
- Age is entered as a number.

If invalid data is entered, an error message is displayed.

---

 How to Run

1. Install Python 3.
2. Save the program as:
   ```
   kriohealth.py
   ```
3. Open Command Prompt or Terminal.
4. Run:
   ```
   python kriohealth.py
   ```

---

 Project Structure

```
KrioHealth/
│
├── kriohealth.py
├── README.md
```

---

 Future Improvements

- Save patient records to a database.
- Search for patients.
- Edit patient information.
- Delete individual patients.
- Generate patient reports.
- Add login authentication.
- Add appointment scheduling.

---

 Author

Amadu Bademba Jagitay

Course Project

Digital Public Good (SDG 3)
