import frappe


def send_capacity_warning(doc, method=None):
    """Notify instructor when a session reaches or exceeds capacity."""
    capacity = getattr(doc, "capacity", 0)
    enrolled = getattr(doc, "enrolled", 0)
    if capacity and enrolled >= capacity:
        instructor = getattr(doc, "instructor", None)
        if instructor:
            try:
                frappe.sendmail(
                    recipients=instructor,
                    subject="Session Capacity Reached",
                    message=f"Session {doc.name} has reached its capacity of {capacity} students.",
                )
            except Exception:
                frappe.log_error("Failed to send capacity warning", "branded_lms")

