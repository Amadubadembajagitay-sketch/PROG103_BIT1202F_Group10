from functions import calculate_wait_time, get_priority

class Patient:
    def __init__(self, name, age, gender, patient_id, condition):
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id
        self.condition = condition
        self.priority = get_priority()

    def get_info(self):
        return f"{self.patient_id} {self.age} {self.gender} {self.condition} {self.priority}"