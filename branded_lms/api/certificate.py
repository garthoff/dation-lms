import frappe
from frappe.utils import getdate

@frappe.whitelist()
def verify_certificate(uuid):
    cert = frappe.db.get("Course Enrollment", {"certificate_uuid": uuid})
    if cert and cert.is_completed:
        return {
            "valid": True,
            "student": cert.student,
            "course": cert.course,
            "completion_date": str(getdate(cert.completion_date))
        }
    return {"valid": False}