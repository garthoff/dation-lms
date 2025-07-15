
def send_completion_email(doc):
    if doc.is_completed and not doc.notified_on_complete:
        template = frappe.render_template("templates/email/course_completion_notification.html", {
            "student_name": doc.student_name,
            "course_name": doc.course,
            "completion_date": doc.completion_date
        })
        frappe.sendmail(
            recipients=[doc.student_email],
            subject="Course Completed",
            message=template
        )
        doc.notified_on_complete = 1
