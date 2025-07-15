import frappe
from frappe.utils import now_datetime
import uuid

def on_course_complete(doc, method):
    if doc.is_completed and not doc.certificate_issued:
        if not doc.certificate_uuid:
            doc.certificate_uuid = str(uuid.uuid4())
        doc.certificate_issued = 1
        doc.completion_date = now_datetime()
        frappe.db.commit()
