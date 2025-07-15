import frappe
from frappe.utils import getdate

@frappe.whitelist()
def verify_certificate(uuid):
    """Return details of a completed course enrollment using the certificate UUID."""

    # Look up the enrollment by its certificate UUID. Using ``get_value`` avoids
    # an exception if the record does not exist.
    enrollment_name = frappe.db.get_value(
        "Course Enrollment", {"certificate_uuid": uuid}, "name"
    )

    if not enrollment_name:
        return {"valid": False}

    cert = frappe.get_doc("Course Enrollment", enrollment_name)
    if cert.is_completed:
        return {
            "valid": True,
            "student": cert.student,
            "course": cert.course,
            "completion_date": str(getdate(cert.completion_date)),
        }

    return {"valid": False}
