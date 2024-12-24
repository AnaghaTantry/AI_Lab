subjects = ["maths", "phy", "che", "bio"]
days = ["Monday", "Tuesday"]
conflicts = [("maths", "phy"), ("che", "bio")]
def scheduleSubjects(assignment):
    if len(assignment) == len(subjects):
        return assignment
    for subject in subjects:
        if subject not in assignment: 
            break   
    for day in days:
        if is_valid_assignment(subject, day, assignment):
            assignment[subject] = day
            result = schedule_subjects(assignment)
            if result:
                return result
            assignment.pop(subject)  
    return None
def is_valid_assignment(subject, day, assignment):
    for (subj1, subj2) in conflicts:
        if subject in (subj1, subj2):
            other_subject = subj1 if subject == subj2 else subj2
            if assignment.get(other_subject) == day:
                return False
    return True
solution = scheduleSubjects({})
print(solution)
 