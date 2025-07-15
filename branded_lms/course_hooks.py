import frappe
from frappe.utils import now_datetime
import uuid


def check_completion_and_send_email(doc, method=None):
    """Issue completion certificate and send notification when a course is completed."""
    if getattr(doc, "is_completed", False) and not getattr(doc, "certificate_issued", False):
        if not getattr(doc, "certificate_uuid", None):
            doc.certificate_uuid = str(uuid.uuid4())
        doc.certificate_issued = 1
        doc.completion_date = now_datetime()
        doc.save(ignore_permissions=True)

        recipient = frappe.db.get_value("Student", doc.student, "email") or doc.student
        try:
            frappe.sendmail(
                recipients=recipient,
                subject="Course Completed",
                message="You have successfully completed the course {}.".format(doc.course),
            )
        except Exception:
            frappe.log_error(f"Failed sending completion email to {recipient}", "branded_lms")

