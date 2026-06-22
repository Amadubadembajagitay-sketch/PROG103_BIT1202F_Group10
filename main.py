import tkinter as tk
from tkinter import messagebox, ttk

class Patient:
    def __init__(self, pid, name, age, condition):
        self.pid = pid
        self.name = name
        self.age = age
        self.condition = condition

    def get_info(self):
        return f"{self.pid} | {self.name} | {self.age} | {self.condition}"

class KrioHealthQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def serve_next(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def get_queue_display(self):
        if not self.queue:
            return "Queue is empty."
        return "\n".join([f"{i+1}. {p.get_info()}" for i, p in enumerate(self.queue)])

# ====================== MAIN GUI ======================
root = tk.Tk()
root.title("KrioHealth Clinic Queue Management System - DPG")
root.geometry("900x650")
root.configure(bg="#0f172a")

queue_system = KrioHealthQueue()
current_patient_label = None

# ================== STYLING ==================
style = ttk.Style()
style.theme_use("clam")

# Header
header = tk.Label(root, text="🩺 KrioHealth Clinic Queue System", font=("Arial", 20, "bold"),
                  bg="#1e2937", fg="#60a5fa", pady=15)
header.pack(fill="x")

# Main Frame
main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Left Frame - Add Patient
left_frame = tk.LabelFrame(main_frame, text=" New Patient ", font=("Arial", 12, "bold"),
                           bg="#1e2937", fg="#e2e8f0", padx=15, pady=15)
left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")

tk.Label(left_frame, text="Patient ID:", bg="#1e2937", fg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
pid_entry = tk.Entry(left_frame, width=30, font=("Arial", 10))
pid_entry.grid(row=0, column=1, pady=5)

tk.Label(left_frame, text="Full Name:", bg="#1e2937", fg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
name_entry = tk.Entry(left_frame, width=30, font=("Arial", 10))
name_entry.grid(row=1, column=1, pady=5)

tk.Label(left_frame, text="Age:", bg="#1e2937", fg="white", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
age_entry = tk.Entry(left_frame, width=30, font=("Arial", 10))
age_entry.grid(row=2, column=1, pady=5)

tk.Label(left_frame, text="Condition:", bg="#1e2937", fg="white", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
condition_entry = tk.Entry(left_frame, width=30, font=("Arial", 10))
condition_entry.grid(row=3, column=1, pady=5)

def add_to_queue():
    pid = pid_entry.get().strip()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    condition = condition_entry.get().strip()

    if not all([pid, name, age, condition]):
        messagebox.showwarning("Missing Info", "Please fill all fields!")
        return

    try:
        patient = Patient(pid, name, int(age), condition)
        queue_system.add_patient(patient)
        update_queue_display()
        clear_fields()
        messagebox.showinfo("Success", f"Patient {name} added to queue!")
    except ValueError:
        messagebox.showerror("Error", "Age must be a number!")

add_btn = tk.Button(left_frame, text="Add to Queue", command=add_to_queue,
                    bg="#22c55e", fg="white", font=("Arial", 11, "bold"), width=20, height=2)
add_btn.grid(row=4, column=0, columnspan=2, pady=15)

# Right Frame - Queue Display + Controls
right_frame = tk.LabelFrame(main_frame, text=" Current Queue ", font=("Arial", 12, "bold"),
                            bg="#1e2937", fg="#e2e8f0", padx=15, pady=15)
right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

queue_text = tk.Text(right_frame, height=15, width=50, bg="#334155", fg="#e0f2fe", font=("Consolas", 11))
queue_text.pack(pady=10)

def update_queue_display():
    queue_text.delete(1.0, tk.END)
    queue_text.insert(tk.END, queue_system.get_queue_display())

def serve_next_patient():
    served = queue_system.serve_next()
    if served:
        messagebox.showinfo("Next Patient", f"Now Serving:\n{served.get_info()}")
        update_queue_display()
    else:
        messagebox.showinfo("Queue Empty", "No patients in queue!")

# Control Buttons
btn_frame = tk.Frame(right_frame, bg="#1e2937")
btn_frame.pack(pady=10)

next_btn = tk.Button(btn_frame, text="👉 Serve Next Patient", command=serve_next_patient,
                     bg="#ef4444", fg="white", font=("Arial", 11, "bold"), width=20, height=2)
next_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear Queue", command=lambda: [queue_system.queue.clear(), update_queue_display()],
                      bg="#64748b", fg="white", font=("Arial", 10))
clear_btn.grid(row=0, column=1, padx=10)

def clear_fields():
    pid_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    condition_entry.delete(0, tk.END)

# Footer
footer = tk.Label(root, text="Digital Public Good (SDG 3) - Improving Healthcare Access",
                  bg="#0f172a", fg="#94a3b8", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()