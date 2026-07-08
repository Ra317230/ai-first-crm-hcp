def log_interaction(data):
    return {"message": "Interaction logged successfully"}

def edit_interaction(id, data):
    return {"message": "Interaction updated successfully"}

def search_hcp(name):
    return {"message": f"HCP '{name}' found"}

def view_history(hcp_id):
    return {"message": f"Showing interaction history for HCP {hcp_id}"}

def schedule_followup(hcp_id, date):
    return {"message": f"Follow-up scheduled on {date}"}