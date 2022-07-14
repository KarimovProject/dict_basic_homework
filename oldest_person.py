def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    #print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, 
    #                 "Sara Pardee": 14, "Fallon Fabiano": 11, 
     #                 "Nidia Dominique": 15})) 
    #return max(people, key=people.get)
    student1 = {"name" : "Abdullatif",  "age" : 19}
    student2 = {"name" : "Maqsud", "age" : 16}
    student3 = {"name" : "Xurshid", "age" : 17}

    student_age = [student1["age"],student2["age"], student3["age"]]
    student_age = sorted(student_age)
    return student_age[2:3]