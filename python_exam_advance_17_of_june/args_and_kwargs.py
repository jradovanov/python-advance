def gather_credits(budget, *args):

    max_credit = 0
    courses = []

    if budget == 0:
        return f"Enrollment finished! Maximum credits: {max_credit}.\nCourses: {', '.join(courses)}"

    is_enough_credits = False

    for course, credit in args:
        if course in courses:
            continue
        else:
            courses.append(course)
            max_credit += int(credit)

        if max_credit >= budget:
            is_enough_credits = True
            break

    if is_enough_credits:
        courses.sort()
        return f"Enrollment finished! Maximum credits: {max_credit}.\nCourses: {', '.join(courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {budget - max_credit} credits more."



print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))