def calculate_wait_time (queue_length):
    """Estimate waiting time (average 10 minutes)"""
    return queue_length / 10

def get_priority(status):
    """simple priority system"""
    if status.lower()=="emergency":
        return "high"
    elif status.lower()=="pregnant":
        return "medium"
    else:
        return "normal"
