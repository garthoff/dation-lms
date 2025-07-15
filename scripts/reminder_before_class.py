
def send_course_reminder():
    from frappe.utils import add_days, nowdate
    sessions = frappe.get_all("Course Session", filters={"session_date": add_days(nowdate(), 2)}, fields=["name", "course", "session_date"])
    for session in sessions:
        students = frappe.get_all("Course Session Attendance", filters={"session": session.name, "present": 0}, fields=["student"])
        for s in students:
            student = frappe.get_doc("Student", s.student)
            if not student.has_completed_homework:
                template = frappe.render_template("templates/email/course_reminder_notification.html", {
                    "student_name": student.full_name,
                    "course_name": session.course,
                    "session_date": session.session_date
                })
                frappe.sendmail(recipients=[student.email], subject="Reminder to complete your course", message=template)
