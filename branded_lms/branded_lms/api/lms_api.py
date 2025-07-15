
import frappe
from frappe import _

@frappe.whitelist()
def get_courses_for_educator(educator):
    return frappe.get_all("Course Access", filters={"educator": educator}, fields=["course", "price_override"])

@frappe.whitelist()
def enroll_student(student, course, company=None, educator=None, enrollment_source="Educator"):
    doc = frappe.get_doc({
        "doctype": "Course Enrollment",
        "student": student,
        "course": course,
        "company": company,
        "educator": educator,
        "enrollment_source": enrollment_source
    })
    doc.insert()
    return {"status": "enrolled", "enrollment": doc.name}

@frappe.whitelist()
def get_student_progress(student):
    return frappe.get_all("Course Enrollment", filters={"student": student}, fields=["course", "is_completed", "completion_date"])

@frappe.whitelist()
def get_company_progress(company):
    return frappe.db.sql("""
        SELECT s.name as student, ce.course, ce.is_completed, ce.completion_date
        FROM `tabStudent` s
        LEFT JOIN `tabCourse Enrollment` ce ON s.name = ce.student
        WHERE s.company = %s
    """, (company,), as_dict=True)
